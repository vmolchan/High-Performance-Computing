#!/usr/bin/env python
import numpy as np

from PyTrilinos import Epetra
from PyTrilinos import AztecOO
from PyTrilinos import Teuchos
from PyTrilinos import Isorropia

class OneDimLaplace(object):

    def __init__(self, comm, number_of_elements=10):

        self.comm = comm
        self.rank = comm.MyPID()
        self.size = comm.NumProc()

        if self.rank == 0:
            number_of_rows = number_of_elements
        else:
            number_of_rows = 0
        
        unbalanced_map = Epetra.Map(-1, number_of_rows, 0, self.comm)

        self.A = Epetra.CrsMatrix(Epetra.Copy, unbalanced_map, 3) 
        self.x = Epetra.Vector(unbalanced_map) 
        self.b = Epetra.Vector(unbalanced_map) 

        for gid in unbalanced_map.MyGlobalElements():
            if gid == 0: 
                self.A.InsertGlobalValues(gid,[1],[gid])
                self.b[0] = -1
            elif gid == (number_of_elements - 1): 
                self.A.InsertGlobalValues(gid,[1],[gid])
                self.b[-1] = 1
            else: 
                self.A.InsertGlobalValues(gid,[-1,2,-1],[gid-1,gid,gid+1])

        #optimizes storage
        self.A.FillComplete()

    def load_balance(self):

        # creating partitioner and redistributing with RCB method
        param_list = Teuchos.ParameterList()
        param_list.set("Partition Method", "Default")
        partitioner = Isorropia.Epetra.Partitioner(self.A,param_list)
        redistributor = Isorropia.Epetra.Redistributor(partitioner)
        self.A = redistributor.redistribute(self.A)
        self.x = redistributor.redistribute(self.x)
        self.b = redistributor.redistribute(self.b)
        
        #print(self.A)
        #print(A_balanced)
        
        # now that its balanced, imp/exp to load balance the other data -> 'x' and 'b'?
        #print(self.A_balanced)
        
        
        
        return


    def solve(self):
        
        # parallel linear solver
        # final project has 2D differential equation
        linearProblem = Epetra.LinearProblem(self.A, self.x, self.b)
        solver = AztecOO.AztecOO(linearProblem)
        solver.Iterate(10000,1.e-5)
        
        return


    def get_solution(self):

        
        return self.x




if __name__ == "__main__":

    from PyTrilinos import Epetra

    comm = Epetra.PyComm()

    solver = OneDimLaplace(comm)
    solver.load_balance()
    solver.solve()

    #print(solver.get_solution())
