from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if min(left, right) == 0:
            minimum = abs(left - right)
        else:
            minimum = min(left, right)

        return minimum + 1