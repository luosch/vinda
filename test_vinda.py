# -*- coding: utf-8 -*-

import unittest
import vinda

class TestVindaMethods(unittest.TestCase):
    def test_current_path(self):
        vinda.look()

    def test_other_path(self):
        pass

if __name__ == '__main__':
    unittest.main()
