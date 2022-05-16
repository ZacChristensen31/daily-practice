from typing import List, Optional

"""
Classic Tree Node, has a value, an optional left TreeNode and an optional right TreeNode 
"""


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Given a list of anything, create a Tree. The root will be index 0, and the left child will be index 1, and the right child will be index 2.
For all further children nodes, the children will be 2x + 1 and 2x + 2, where x is the index of the parent node.
"""


class Tree:

    def __init__(self, tree_as_list: List):
        self.tree_as_list = tree_as_list
        self.root = self.generate_tree_node(0)

    def generate_tree_node(self, index: int) -> Optional[TreeNode]:
        if index >= len(self.tree_as_list) or self.tree_as_list[index] is None:
            return None
        else:
            return TreeNode(self.tree_as_list[index], self.generate_tree_node(2 * index + 1),
                            self.generate_tree_node(2 * index + 2))
