from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def dfs(self, node: Optional[TreeNode]):
        if not node:
            return

        self.path.append(str(node.val))
        if not node.left and not node.right:
            tmp = '->'.join(self.path)
            self.res.append(tmp)

        self.dfs(node.left)
        self.dfs(node.right)

        self.path.pop()

        return

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.dfs(root)
        return self.res


