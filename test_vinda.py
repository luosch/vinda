# -*- coding: utf-8 -*-
import unittest
import vinda

class TestVindaMethods(unittest.TestCase):
    
    def test_default_path(self):
        vinda.look(ignore=['.git', '.DS_Store', 'dist'])

    def test_specific_path(self):
        vinda.look(path='dist', ignore=['.git', '.DS_Store'])


if __name__ == '__main__':
    unittest.main()
