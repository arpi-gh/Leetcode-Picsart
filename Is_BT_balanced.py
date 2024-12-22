from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# old solution
# class Solution:
#     def getHeight(self, node) -> int:
#         if not node:
#             return 0
#         left = self.getHeight(node.left)
#         right = self.getHeight(node.right)
#
#         return max(left, right) + 1
#
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
#
#         if not -1 <= self.getHeight(root.left) - self.getHeight(root.right) <= 1:
#             return False
#
#         return self.isBalanced(root.left) and self.isBalanced(root.right)

# new solution
class Solution:
    def __init__(self):
        self.res = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(node):
            if not node:
                return 0
            left = getHeight(node.left)
            right = getHeight(node.right)

            if abs(left - right) > 1:
                self.res = False

            return 1 + max(left, right)

        if not root:
            return True

        getHeight(root)
        return self.res