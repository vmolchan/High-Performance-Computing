#!/usr/bin/env python

import os
import unittest
import numpy as np

from PyTrilinos import Epetra
from assignment20 import OneDimNonliear

class TestOneDimNonlinear(unittest.TestCase):

    def setUp(self):

        self.comm = Epetra.PyComm()
        self.rank = self.comm.MyPID()

    def test_nonlinear(self):
        
        solver = OneDimNonliear(self.comm, nx=10, k=10)
        solver.solve()
        sol = solver.get_final_solution()
        if self.rank == 0:
            np.testing.assert_allclose(sol, np.array([0., 0.06673361, 0.13401702, 0.20351778, 0.27813205, 0.36229663, 0.462666,  0.58946252, 0.75915608, 1.]), atol=0.01) 


if __name__ == '__main__':
    unittest.main()
