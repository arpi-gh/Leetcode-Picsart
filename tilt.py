from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.tilt = 0

    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.tilt += abs(left - right)

        return left + right + node.val

    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.dfs(root)
        return self.tilt


