#!/usr/bin/env python
from assignment8 import StressStrainConverter
import numpy as np
import scipy.integrate

from PyTrilinos import Epetra

class EpetraParallelToughness(StressStrainConverter):

    def __init__(self, filename, comm):
        super().__init__(filename)
        
        self.comm = comm
        self.rank = comm.MyPID()
        self.size = comm.NumProc()

        if self.rank == 0:
            self.convert_to_true_stress_and_strain()
        else:
            self.true_stress = np.array([], dtype=np.double)
            self.true_strain = np.array([], dtype=np.double)
        
        unbalanced_map = Epetra.Map(-1, len(self.true_stress), 0, self.comm)
        unbalanced_stress = Epetra.Vector(Epetra.View, unbalanced_map, self.true_stress)
        unbalanced_strain = Epetra.Vector(Epetra.View, unbalanced_map, self.true_strain)
        
        balanced_map = self.create_balanced_map(unbalanced_map)
        
        importer = Epetra.Import(balanced_map,unbalanced_map)
        
        self.true_stress = Epetra.Vector(balanced_map)
        self.true_strain = Epetra.Vector(balanced_map)
        
        self.true_stress.Import(unbalanced_stress, importer, Epetra.Insert)
        self.true_strain.Import(unbalanced_strain, importer, Epetra.Insert)
        
    def create_balanced_map(self,unbalanced_map):
        
        temp_map = Epetra.Map(unbalanced_map.NumGlobalElements(), 0, self.comm)
        #print(temp_map)
        my_global_element_list = temp_map.MyGlobalElements()
        
        if self.rank < (self.size - 1):
            my_global_element_list = np.append(my_global_element_list, [temp_map.MaxMyGID()+1])
        
        
        return Epetra.Map(-1,list(my_global_element_list), 0, self.comm)
     

    def compute_toughness(self):

        
        my_toughness = scipy.integrate.trapz(self.true_stress, self.true_strain)

        return self.comm.SumAll(my_toughness)


if __name__ == "__main__":

    from PyTrilinos import Epetra

    comm = Epetra.PyComm()

    T = EpetraParallelToughness('data.dat', comm)

    if comm.MyPID() == 0:
        print(T.compute_toughness())

        
                # need unbalanced vector stress and strain
        # this gets exported to the balanced vector y
        # y will be the partitioned data that we can do the inegration over
        #globalStressLength = len(self.true_stress)
        #globalStrainLength = len(self.true_strain)
        
        #all_stress = np.array_split(self.true_stress,self.size)
        #all_strain = np.array_split(self.true_strain,self.size)
        
        #if self.rank == 0:
        #    myStressLength = len(self.true_stress)
        #    myStrainLength = len(self.true_strain)
        #else:
        #    myStressLength = 0
        #    myStrainLength = 0
        #
        #myStressLength = len(all_stress[self.rank])
        #myStrainLength = len(all_strain[self.rank])
        
        #stdStessMap = Epetra.Map(globalStressLength,myStressLength,0,self.comm)
        #stdStrainMap = Epetra.Map(globalStrainLength,myStrainLength,0,self.comm)
          
        #stdBalancedStessMap = Epetra.Map(globalStressLength,0,self.comm)
        #stdBalancedStrainMap = Epetra.Map(globalStrainLength,0,self.comm)
        
        #x_stress = Epetra.Vector(stdStessMap, self.true_stress)
        #x_strain = Epetra.Vector(stdStrainMap, self.true_strain)
        
        #self.true_stress = Epetra.Vector(stdBalancedStessMap)
        #self.true_strain = Epetra.Vector(stdBalancedStrainMap)
        
        #importer_stress = Epetra.Import(stdBalancedStessMap,stdStessMap)
        #importer_strain = Epetra.Import(stdBalancedStrainMap,stdStrainMap)
        
        #self.true_stress.Import(x_stress,importer_stress, Epetra.Insert)
        #self.true_strain.Import(x_strain,importer_strain, Epetra.Insert)
        
        #self.true_stress = y_stress
        #self.true_strain = y_strain
        #print(self.true_stress)