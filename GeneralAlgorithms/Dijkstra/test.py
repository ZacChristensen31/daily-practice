import unittest

from GeneralAlgorithms.Dijkstra.dijkstra import shortest_path_dijkstra


class MyTestCase(unittest.TestCase):
    def test_empty_case(self):
        edges = []
        self.assertEqual(shortest_path_dijkstra(edges, 1, 2), (-1, []))

    def test_simple_case(self):
        edges = [[1, 2, 4]]
        self.assertEqual(shortest_path_dijkstra(edges, 1, 2), (4, [1, 2]))

    def test_complex_case(self):
        edges = [[1, 4, 10], [1, 2, 1], [2, 3, 2], [3, 4, 3]]
        self.assertEqual(shortest_path_dijkstra(edges, 1, 4), (6, [1, 2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
