from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_sum = None

    def dfs(self, node):
        if not node:
            return 0

        left = max(self.dfs(node.left), 0)
        right = max(self.dfs(node.right), 0)

        self.max_sum = max((left + right + node.val), self.max_sum)

        return max(left, right) + node.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = root.val
        self.dfs(root)
        return self.max_sum
