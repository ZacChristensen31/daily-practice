import unittest

from GeneralAlgorithms.DFS.dfs import dfs


class MyTestCase(unittest.TestCase):
    def test_empty_path(self):
        edges = []
        self.assertEqual(dfs(edges, 1, 2), (-1, []))

    def test_simple_path(self):
        edges = [[1, 2]]
        self.assertEqual(dfs(edges, 1, 2), (1, [1, 2]))

    def test_moderate_path(self):
        edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7]]
        self.assertEqual(dfs(edges, 1, 6), (2, [1, 3, 6]))

    def test_complex_path(self):
        edges = [[1, 2], [1, 3], [1, 4], [2, 5], [2, 6], [5, 9], [5, 10], [4, 7], [4, 8], [7, 11], [7, 12]]
        self.assertEqual(dfs(edges, 1, 12), (3, [1, 4, 7, 12]))

    def test_multiple_paths(self):
        edges = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 5], [3, 4], [3, 5], [4, 7], [5, 7]]
        self.assertEqual(dfs(edges, 1, 7), (4, [1, 2, 3, 4, 7]))


if __name__ == '__main__':
    unittest.main()
