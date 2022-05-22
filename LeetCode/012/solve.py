# Problem comes from LeetCode
# Solved on Saturday May 21st, 2022
from typing import Optional
from GeneralAlgorithms.Tree.tree import TreeNode, Tree

"""
    Given two binary tree nodes, return if they are equal
"""
def solve(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None or q == None:
            return p == None and q == None

        if p.val != q.val:
            return False

        return solve(p.left, q.left) and solve(p.right, q.right)

if __name__ == '__main__':
    a = Tree([1, 2, 3, 4, 5, 6, 7])
    b = Tree([1, 2, 3, 4, 5, 6, 7])
    assert solve(a.root, b.root) is True

    c = Tree([1, 2, 3, 4, 5])
    d = Tree([1, 2, 3, 5, 4])
    assert solve(c.root, d.root) is False

    e = Tree([1, 2, 3])
    f = Tree([1, 2, 3, 4])
    assert solve(e.root, f.root) is False

