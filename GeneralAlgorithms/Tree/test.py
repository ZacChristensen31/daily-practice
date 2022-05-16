import unittest

from GeneralAlgorithms.Tree.tree import Tree


class MyTestCase(unittest.TestCase):
    def test_initialization(self):
        tree = Tree([1, 2, 3, 4, 5, 6, 7])
        root = tree.root
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.left.left.val, 4)
        self.assertEqual(root.left.right.val, 5)
        self.assertEqual(root.right.left.val, 6)
        self.assertEqual(root.right.right.val, 7)

    def test_empty_nodes(self):
        tree = Tree([1, None, 3, None, None, None, 7])
        root = tree.root
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left, None)
        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.right.left, None)
        self.assertEqual(root.right.right.val, 7)



if __name__ == '__main__':
    unittest.main()
