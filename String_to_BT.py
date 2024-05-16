from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = ''

    def dfs(self, node):
        if not node:
            return

        self.res += f'{node.val}'

        if node.left:
            self.res += '('
        elif node.right:
            self.res += '()'

        self.dfs(node.left)
        if node.right:
            self.res += '('
        self.dfs(node.right)
        self.res += ')'

        return

    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.dfs(root)
        return self.res[:-1]





