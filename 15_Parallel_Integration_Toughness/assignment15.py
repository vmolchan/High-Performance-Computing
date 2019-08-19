#!/usr/bin/env python
from assignment8 import StressStrainConverter
import numpy as np
import scipy.integrate
from mpi4py import MPI

class ParallelToughness(StressStrainConverter):

    def __init__(self, filename, comm):
        super().__init__(filename)

        self.comm = comm
        self.rank = comm.rank
        self.size = comm.size

        if self.rank == 0:
            self.convert_to_true_stress_and_strain()
        else:
            self.true_stress = []
            self.true_strain = []
        
        send_buf_1 = []
        send_buf_2 = []
        
        if self.rank == 0:
            send_buf_1 = np.array_split(self.true_strain,self.size)
            send_buf_2 = np.array_split(self.true_stress,self.size)
            
        self.true_strain = self.comm.scatter(send_buf_1, root=0) 
        self.true_stress = self.comm.scatter(send_buf_2, root=0) 
        
        
        if self.rank > 0:
            self.comm.send(self.true_strain[0], dest=(self.rank - 1), tag=0)
            self.comm.send(self.true_stress[0], dest=(self.rank - 1), tag=1)
        if self.rank < (self.size - 1):
            last_point1 = self.comm.recv(source=(self.rank+1), tag=0)
            last_point2 = self.comm.recv(source=(self.rank+1), tag=1)
            self.true_strain = np.append(self.true_strain, last_point1)
            self.true_stress = np.append(self.true_stress, last_point2)
        
        
        #stress = self.partition_data(self.true_stress)
        #strain = self.partition_data(self.true_strain)
         

    def partition_data(self, data):
        if self.rank == 0:
            send_buf = np.array_split(data, self.size)
            data = comm.scatter(send_buf, root=0)
            #for i in range(1,self.size):
            #    np.append(send_buf[i-1], send_buf[i][0])
            
        else:
            send_buf = []
        
        
        if self.rank > 0:
            comm.send(data[0], dest=(self.rank - 1))
        if self.rank < (self.size - 1):
            last_point = comm.recv(source=(self.rank + 1))
            np.append(stress,last_point)
            
    def compute_toughness(self):
       
        
        my_toughness = scipy.integrate.trapz(self.true_stress, self.true_strain)
        
        recvbuf = self.comm.reduce(my_toughness,root=0)
        if self.comm.rank == 0:
            return np.sum(np.array(recvbuf))
        
        return
