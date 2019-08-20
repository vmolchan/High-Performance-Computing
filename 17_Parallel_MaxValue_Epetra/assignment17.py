#!/usr/bin/env python
import numpy as np

from PyTrilinos import Epetra

class Max():

    def __init__(self, basename, comm):

        self.comm = comm
        self.rank = comm.MyPID()
        self.size = comm.NumProc()

    #def load_data(self)
    #    df = np.loadtxt('ss.' + str(self.rank) + '.' + str(self.size) + '.dat')
        
    #    stress = df[:,1]
    #    stress_len = stress.shape[0]
        
    #    stdMap = Epetra.Map(-1,stress_len,0,self.comm)
        
    #    self.stress = Epetra.Vector(stdMap,stress)
        
    
    def get_max(self):
        df = np.loadtxt('ss.' + str(self.rank) + '.' + str(self.size) + '.dat')
        
        stress = df[:,1]
        stress_len = stress.shape[0]
        
        stdMap = Epetra.Map(-1,stress_len,0,self.comm)
        
        self.stress = Epetra.Vector(Epetra.View, stdMap,stress)


        #df = np.loadtxt('ss.%s.4.dat' % self.rank)
        #df = np.array([[np.int32(df[i,j]) for j in range(len(df[0,:]))] for i in range(len(df[:,0]))])
        #df = df[:,1]

        #stdMap = Epetra.Map(12243, df, 0, self.comm)
        #self.stress = Epetra.Vector(stdMap)
        #print(self.stress)
        
        #print(str(stdMap.MyGlobalElements()))
        
        
        
        return self.stress.MaxValue()[0]




if __name__ == "__main__":

    from PyTrilinos import Epetra

    comm = Epetra.PyComm()

    T = Max('ss', comm)

    print(T.get_max())
