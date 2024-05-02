from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.tree = []

    def inorderTraversal(self, root: Optional[TreeNode]):
        if not root:
            return
        self.inorderTraversal(root.left)
        self.tree.append(root.val)
        self.inorderTraversal(root.right)
        return self.tree


node = TreeNode(1)
print(Solution().inorderTraversal(root=node))
