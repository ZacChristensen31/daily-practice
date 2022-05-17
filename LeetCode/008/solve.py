# Problem comes from LeetCode https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
# Solved on Tuesday May 17th, 2022
from typing import Optional

from GeneralAlgorithms.Tree.tree import Tree, TreeNode

"""
    Given two binary trees original and cloned and given a reference to a node target in the original tree.
    We want to return the reference to the same node in the cloned tree.

    Inputs:
        - original: a binary tree node
        - cloned: a binary tree node
        - target: a binary tree node

    Output:
        - a binary tree node OR None
"""


def solve(original_node: TreeNode, cloned_node: TreeNode, target_node: TreeNode) -> Optional[TreeNode]:
    if original_node is None:
        return None
    if original_node == target_node:
        return cloned_node
    else:
        return solve(original_node.left, cloned_node.left, target_node) or solve(original_node.right, cloned_node.right,
                                                                                 target_node)


if __name__ == '__main__':
    original = Tree([7, 4, 3, None, None, 6, 19]).root
    cloned = Tree([7, 4, 3, None, None, 6, 19]).root
    target = original.left.right
    assert solve(original, cloned, target) == cloned.left.right

    original = Tree([8, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]).root
    cloned = Tree([8, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]).root
    target = original.right.right.right
    assert solve(original, cloned, target) == cloned.right.right.right
