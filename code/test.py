#! /usr/local/bin/python3


import unittest
import array_and_string as aas

class TestArrayAndString(unittest.TestCase):
    def test_is_unique(self):
        self.assertTrue(aas.is_unique('abdhujsik'))
        self.assertFalse(aas.is_unique('aaaaa'))
        self.assertFalse(aas.is_unique(''))




if __name__ == '__main__':
    unittest.main()