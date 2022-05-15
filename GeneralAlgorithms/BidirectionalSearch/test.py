import unittest

from GeneralAlgorithms.BidirectionalSearch.bidirectional_search import bidirectional_search


class MyTestCase(unittest.TestCase):
    def test_simple_caseo(self):
        edges = [[1, 2, 1], [1, 3, 1], [2, 4, 1], [2, 5, 1], [3, 6, 1], [3, 7, 1], [4, 8, 1]]
        output = bidirectional_search(edges, 1, 8)
        self.assertEqual(output, (3, [1, 2, 4, 8]))

    def test_weighted_case(self):
        edges = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [1, 8, 2], [8, 9, 1], [9, 10, 4], [10, 7, 3]]
        output = bidirectional_search(edges, 1, 7)
        self.assertEqual(output, (6, [1, 2, 3, 4, 5, 6, 7]))

if __name__ == '__main__':
    unittest.main()
