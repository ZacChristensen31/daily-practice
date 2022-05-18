# Problem comes from LeetCode: https://leetcode.com/problems/deepest-leaves-sum/
# Solved on Sunday May 15th, 2022
from typing import Optional, Tuple

from GeneralAlgorithms.Tree.tree import TreeNode


def nifty_solve(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    depth_map = {}

    def traverse(node: TreeNode, depth: int):
        if node is None:
            return

        if depth not in depth_map.keys():
            depth_map[depth] = node.val
        else:
            depth_map[depth] += node.val

        traverse(node.left, depth + 1)
        traverse(node.right, depth + 1)

    traverse(root, 0)
    return depth_map[max(depth_map.keys())]


def solve(root: Optional[TreeNode]) -> int:
    return _recurse(root, 0)[0]


def _recurse(start_node: Optional[TreeNode], depth: int) -> Tuple[int, int]:
    if start_node.left is None and start_node.right is None:
        return start_node.val, depth

    left_val, right_val = 0, 0
    left_depth, right_depth = depth, depth
    if start_node.left is not None:
        left_val, left_depth = _recurse(start_node.left, depth + 1)
    if start_node.right is not None:
        right_val, right_depth = _recurse(start_node.right, depth + 1)

    if left_depth == right_depth:
        return left_val + right_val, left_depth
    elif left_depth > right_depth:
        return left_val, left_depth
    else:
        return right_val, right_depth


def small_test(target_solve=solve):
    a = TreeNode(8)
    b = TreeNode(5)
    root = TreeNode(1, left=a, right=b)

    assert target_solve(root) == 13
    print('Small Test Passed!')


def single_deep_node_test(target_solve=solve):
    d = TreeNode(7)
    c = TreeNode(5, left=d)
    b = TreeNode(4, left=c)
    a = TreeNode(5)
    root = TreeNode(1, left=a, right=b)

    assert target_solve(root) == 7
    print('Single Deep Node Test Passed!')


def leet_code_test(target_solve=solve):
    g = TreeNode(8)
    f = TreeNode(7)
    e = TreeNode(6, right=g)
    d = TreeNode(5)
    c = TreeNode(4, left=f)
    b = TreeNode(3, left=e)
    a = TreeNode(2, left=c, right=d)
    root = TreeNode(1, left=a, right=b)

    assert target_solve(root) == 15
    print('Leet Code Test Passed!')


if __name__ == '__main__':
    small_test(nifty_solve)
    single_deep_node_test(nifty_solve)
    leet_code_test(nifty_solve)
