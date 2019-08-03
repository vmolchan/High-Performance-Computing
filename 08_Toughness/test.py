#!/usr/bin/env python


import numpy as np
import unittest


from assignment8 import Toughness

class TestSolution(unittest.TestCase):

    def test_toughness(self):

        ss = Toughness('data.dat')

        np.testing.assert_allclose(ss.compute_toughness_simps(), 70836.23, atol=0.01)
        np.testing.assert_allclose(ss.compute_toughness_trapz(), 70836.14, atol=0.01)

        
if __name__ == '__main__':
    unittest.main()

