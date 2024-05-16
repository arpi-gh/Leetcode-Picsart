from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.prev = None
        self.diff = None
        self.min_diff = 10 ** 8

    def getMinimumDifference(self, node: Optional[TreeNode]) -> int:
        if not node:
            return

        self.getMinimumDifference(node.left)
        if self.prev is None:
            self.prev = node.val
        else:
            self.diff = node.val - self.prev

        if self.diff is not None and self.diff < self.min_diff:
            self.min_diff = self.diff

        self.prev = node.val

        self.getMinimumDifference(node.right)

        return self.min_diff

