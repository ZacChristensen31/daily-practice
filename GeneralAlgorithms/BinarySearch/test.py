import unittest

from GeneralAlgorithms.BinarySearch.binary_search import binary_search


class MyTestCase(unittest.TestCase):
    def test_empty_search(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_single_element(self):
        self.assertEqual(binary_search([1], 1), 0)
        self.assertEqual(binary_search([1], 2), -1)

    def test_larger_list(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1), 0)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), 1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4), 3)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 4)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6), 5)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7), 6)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8), 7)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9), 8)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 9)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0), -1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), -1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1), -1)


if __name__ == '__main__':
    unittest.main()
