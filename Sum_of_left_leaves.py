from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sum = 0

    def sumOfLeftLeaves(self, node: Optional[TreeNode], left=False) -> int:
        if node is None:
            return

        if left and (not node.left and not node.right):
            self.sum += node.val

        self.sumOfLeftLeaves(node.left, left=True)
        self.sumOfLeftLeaves(node.right, left=False)

        return self.sum
