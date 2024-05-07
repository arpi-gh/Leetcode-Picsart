from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def __init__(self):
#         self.stack =[]
#         self.res = []
    # def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root:
    #         return

    #     self.postorderTraversal(root.left)
    #     self.postorderTraversal(root.right)

    #     self.res.append(root.val)

    #     return self.res
class Solution:
    def __init__(self):
        self.stack =[]
        self.res = []

    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        self.stack.append(root)
        while len(self.stack):
            cur = self.stack.pop()
            self.res.append(cur.val)
            if cur.left:
                self.stack.append(cur.left)
            if cur.right:
                self.stack.append(cur.right)

        self.res.reverse()
        return self.res