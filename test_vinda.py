# -*- coding: utf-8 -*-

import unittest
import vinda

class TestVindaMethods(unittest.TestCase):
    def test_default_parameter(self):
        vinda.look()

    def test_non_default_parameter(self):
        ignore_list=['.git', '.DS_Store', '.gitignore']
        vinda.look(root_path='.', output_path='index.html', ignore_list=ignore_list)

if __name__ == '__main__':
    unittest.main()
