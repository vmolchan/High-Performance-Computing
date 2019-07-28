#/usr/bin/env python

import unittest

class TestSolution(unittest.TestCase):
    
    def clean_parse(self, filename):

        with open(filename) as f:

            lines = f.readlines()

        clean_lines = [ line.strip().split() for line in lines ]

        return clean_lines

    def test_parse1(self):

        clean_lines = self.clean_parse('grep1.out')

        assert ['1.473248', '2.027327'] in clean_lines
        assert ['2.027327', '1.473248'] in clean_lines
        

    def test_parse2(self):

        clean_lines = self.clean_parse('grep2.out')

        assert ['1.473248', '2.027327'] in clean_lines
        


if __name__ == '__main__':
    unittest.main()
