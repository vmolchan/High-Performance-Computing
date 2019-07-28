#/usr/bin/env python

import unittest
import os 

class TestSolution(unittest.TestCase):
    
    def test_for_files1_lorem2(self):

        assert os.path.isfile('./files1/lorem2.txt')

    def test_for_files1_lorem3(self):

        assert os.path.isfile('./files1/lorem3.txt')

    def test_for_files2_lorem2(self):

        assert os.path.isfile('./files2/lorem2.txt')

    def test_for_files2_lorem3(self):

        assert os.path.isfile('./files2/lorem3.txt')

    def test_lorem3_content_1(self):

        with open('./files1/lorem3.txt') as f:

            lines = f.readlines()

        assert lines[9][6:13] == 'numquam'

    def test_lorem3_content_2(self):

        with open('./files2/lorem3.txt') as f:

            lines = f.readlines()

        assert lines[7][17:22] == 'velit'


if __name__ == '__main__':
    unittest.main()

