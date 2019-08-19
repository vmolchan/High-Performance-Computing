#!/usr/bin/env python

import os.path
import unittest

class TestSolution(unittest.TestCase):

    def test_plot_0(self):
        assert os.path.isfile('plot_0.png')

    def test_plot_1(self):
        assert os.path.isfile('plot_1.png')

        
if __name__ == '__main__':
    unittest.main()
    
