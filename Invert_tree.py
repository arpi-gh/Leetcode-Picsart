from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert(self, node):
        if not node:
            return

        node.left, node.right = node.right, node.left

        self.invertTree(node.left)
        self.invertTree(node.right)

        return

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root

