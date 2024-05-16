from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = []
        self.count = 0
        self.max_count = 0
        self.prev = None

    def dfs(self, node):
        if not node:
            return

        self.dfs(node.left)

        if self.prev is None:
            self.prev = node.val

        if node.val == self.prev:
            self.count += 1
        else:
            self.count = 1

        if self.count > self.max_count:
            self.res = []
            self.res.append(node.val)
            self.max_count = self.count
        elif self.count == self.max_count:
            self.res.append(node.val)

        self.prev = node.val

        self.dfs(node.right)

        return

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root)
        return self.res



