#!/usr/bin/env python
import numpy as np
import scipy.integrate

from mpi4py import MPI

class GaussTable():

    def __init__(self, function, integration_limits, comm):

        self.comm = comm
        self.rank = comm.rank
        self.size = comm.size
        self.next_order = 1

        self.function = function
        self.integration_limits = integration_limits

        self.my_table = []

    def generate_table(self, N):
        # Implement boss/worker parallel Gauss integration scheme here
        """
            Use fixed_quad() to numerically evaluate integrals:
            
            scipy.integrate.fixed_quad(func, a, b, args=(), n=5)
            Compute a definite integral using fixed-order Gaussian quadrature
            Integrate func from a to b using Gaussian quadrature of order n.
            
            Can only use send(), isend(), recv(), gather. Use to generate a table of Gauss points and                         corresponding value of integral from 1:50. 
            
            Use boss/worker model where rank 0 assigns work to non-busy processors.
            
            Each rank will store a list [integration order, integration value] in self.my_table
            
        """
        
        #send to first processor
        
           
        for i in range(1,N+1):
            #send data to any open processor
            if self.rank == 0:
                free_processor = self.comm.recv(source=MPI.ANY_SOURCE)
                self.comm.isend(i,dest=free_processor)

                
            else:
                self.comm.send(self.rank, dest=0)
                order = self.comm.recv(source=0)
                if order == -1:
                    break
                integral_calc, _ = scipy.integrate.fixed_quad(
                    self.function,self.integration_limits[0],self.integration_limits[1], [],order)
                self.my_table += [[order, integral_calc]]
                
        if self.comm.size > 2:
            if self.rank == 0:
                for _ in range(self.comm.size-1):
                    free_processor = self.comm.recv(source=MPI.ANY_SOURCE)
                    self.comm.isend(-1,dest=free_processor)
                    
        
        return self.clean_table(self.comm.gather(self.my_table, root=0))


    def clean_table(self, table):
        """ Removes empty table entries ([]) and sorts results """
        clean_table = []
        if self.rank == 0:
            for item in table:
                if item != []:
                    for item in item:
                        clean_table += [item]

        return sorted(clean_table) 

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    gi = GaussTable(lambda x: x ** 2. * np.exp(-x ** 2.), (0, 1), comm)
    table = gi.generate_table(10)
    if comm.rank == 0:
        print(table)