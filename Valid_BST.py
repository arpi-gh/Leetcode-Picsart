from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @staticmethod
    def check_validity(node, left_boundary=float(-inf), right_boundary=float(inf)):
        if not node:
            return True
        if not (left_boundary < node.val < right_boundary):
            return False
        return (Solution().check_validity(node.left, left_boundary=left_boundary, right_boundary=node.val) and
                Solution().check_validity(node.right, left_boundary=node.val, right_boundary=left_boundary))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return Solution().check_validity(root)


node5 = TreeNode(5)
node1 = TreeNode(1)
node4 = TreeNode(4)
node3 = TreeNode(3)
node6 = TreeNode(6)

node5.left = node1
node5.right = node4
node4.left = node3
node4.right = node6

print(Solution().isValidBST(node5))
