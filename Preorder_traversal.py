from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = []
        self.stack = []

    def preorderTraversal(self, root: Optional[TreeNode]):
        if root is None:
            return

        self.res.append(root.val)

        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.res

    def iterPreorderTraversal(self, root: Optional[TreeNode]):
        if not root:
            return []
        self.stack.append(root)
        while len(self.stack):
            cur = self.stack.pop()
            if cur.right:
                self.stack.append(cur.right)
            if cur.left:
                self.stack.append(cur.left)
            self.res.append(cur.val)
        return self.res







