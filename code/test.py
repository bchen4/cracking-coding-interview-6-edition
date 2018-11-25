#! /usr/local/bin/python3


import unittest
import array_and_string as aas


class TestArrayAndString(unittest.TestCase):

    def test_is_unique(self):
        self.assertTrue(aas.is_unique('abdhujsik'))
        self.assertFalse(aas.is_unique('aaaaa'))
        self.assertFalse(aas.is_unique(''))

    def test_check_permutation(self):
        self.assertTrue(aas.check_permutation('aabbccdd', 'abcdabcd'))
        self.assertTrue(aas.check_permutation('a', 'a'))
        self.assertTrue(aas.check_permutation('', ''))
        self.assertFalse(aas.check_permutation('abcdef', 'abcdff'))

    def test_urlify(self):
        self.assertEqual(aas.urlify("This is an apple       ", 16), "This%20is%20an%20apple")


if __name__ == '__main__':
    unittest.main()