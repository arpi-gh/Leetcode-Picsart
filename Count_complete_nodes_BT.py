from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def countNodes(self, node: Optional[TreeNode]) -> int:
    #     if not node:
    #         return 0

    #     left = self.countNodes(node.left)
    #     right = self.countNodes(node.right)

    #     return left + right + 1

    def getLeftHeight(self, node):
        if not node:
            return 0
        h = self.getLeftHeight(node.left)
        return h + 1

    def getRightHeight(self, node):
        if not node:
            return 0
        h = self.getRightHeight(node.right)
        return h + 1

    def countNodes(self, root: Optional[TreeNode]) -> int:
        left = self.getLeftHeight(root)
        right = self.getRightHeight(root)
        if left == right:
            return (2 ** left) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
