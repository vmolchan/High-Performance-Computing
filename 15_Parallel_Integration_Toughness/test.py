#!/usr/bin/env python
import os
import unittest
from mpi4py import MPI

from assignment15 import ParallelToughness

class TestParallelToughness(unittest.TestCase):

    def setUp(self):

        comm = MPI.COMM_WORLD
        self.T = ParallelToughness('data.dat', comm)

    def test_compute_toughness(self):

        toughness = self.T.compute_toughness()

        if self.T.comm.rank == 0:
            self.assertAlmostEqual(toughness, 70836.14348345132, 2)


if __name__ == '__main__':
    unittest.main()
