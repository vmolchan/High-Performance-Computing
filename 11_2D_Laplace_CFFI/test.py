#!/usr/bin/env python

from laplace import LaplaceSolver
import numpy as np
import unittest
import time


class TestSolution(unittest.TestCase):

    def test_top_bc(self):

        solver = LaplaceSolver(nx=4, ny=3)
        solver.set_boundary_condtion('top', lambda x,y: 10)
        solver.cffi_solve_api(quiet=True)
        x = solver.get_solution()
        solver.reset()
        solver.solve(quiet=True)
        y = solver.get_solution()
        np.testing.assert_allclose(x, y, atol=0.01)


    def test_left_bc(self):

        solver = LaplaceSolver(nx=4,ny=4)
        solver.set_boundary_condtion('left', lambda x,y: 7)
        solver.cffi_solve_api(quiet=True)
        x = solver.get_solution()
        solver.reset()
        solver.solve(quiet=True)
        y = solver.get_solution()
        np.testing.assert_allclose(x, y, atol=0.01)


    def test_right_bc(self):

        solver = LaplaceSolver(nx=4,ny=3)
        solver.set_boundary_condtion('right', lambda x,y: 5)
        solver.cffi_solve_api(quiet=True)
        x = solver.get_solution()
        solver.reset()
        solver.solve(quiet=True)
        y = solver.get_solution()
        np.testing.assert_allclose(x, y, atol=0.01)


    def test_bottom_bc(self):
        solver = LaplaceSolver(nx=3,ny=3)
        solver.set_boundary_condtion('bottom', lambda x,y: 14)
        solver.cffi_solve_api(quiet=True)
        x = solver.get_solution()
        solver.reset()
        solver.solve(quiet=True)
        y = solver.get_solution()
        np.testing.assert_allclose(x, y, atol=0.01)
        
        
    def test_timing(self):
        
        solver = LaplaceSolver()
        solver.set_boundary_condtion('top', lambda x,y: 10)
        solver.set_boundary_condtion('bottom', lambda x,y: 10)
        start = time.time()
        solver.solve(quiet=True)
        end = time.time()
        t1 = end - start
        solver.reset()
        start = time.time()
        solver.cffi_solve_api(quiet=True)
        end = time.time()
        t2 = end - start
        
        assert t1 / t2 > 10.0
        
        
        
if __name__ == '__main__':
        unittest.main()
