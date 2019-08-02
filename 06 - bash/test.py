#/usr/bin/env python

#/usr/bin/env python

import unittest

class TestSolution(unittest.TestCase):
    
    def test_lla(self):

        with open('lla.txt', 'r') as f:

            first_line = f.readline()
            split_line = first_line.rstrip().split()

            assert split_line[0] == 'alias'
            assert split_line[1] == "lla='ls"
            assert split_line[2] == "-la'"


if __name__ == '__main__':
    unittest.main()