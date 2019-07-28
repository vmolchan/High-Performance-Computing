#/usr/bin/env python

import unittest

class TestSolution(unittest.TestCase):
    
    def test_myfind(self):

        with open('./find.out') as f:

            lines = f.readlines()

        assert './files1/lorem3.dat\n' in lines
        assert './files2/lorem2.dat\n' in lines
        
if __name__ == '__main__':
    unittest.main()




