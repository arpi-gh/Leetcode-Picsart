from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def dfs(node1, node2) -> bool:
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        elif node1.val != node2.val:
            return False

        return Solution().dfs(node1.left, node2.right) and Solution().dfs(node1.right, node2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return Solution().dfs(root.left, root.right)
