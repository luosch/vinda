# -*- coding: utf-8 -*-
import unittest
import vinda

class TestVindaMethods(unittest.TestCase):
    def test_vinda(self):
        vinda.look(ignore=['.git', '.DS_Store'])

if __name__ == '__main__':
    unittest.main()
