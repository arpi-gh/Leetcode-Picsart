from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.cur_sum = 0
        self.found = False

    def dfs(self, node, target_sum):
        if not node:
            return

        self.cur_sum += node.val
        if not node.left and not node.right:
            if self.cur_sum == target_sum:
                self.found = True
                return

        self.hasPathSum(node.left, target_sum)
        self.hasPathSum(node.right, target_sum)

        self.cur_sum -= node.val

        return

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.dfs(root, targetSum)
        return self.found

# Doesn't work
# class Solution:
#     def __init__(self):
#         self.cur_sum = 0
#
#
#     def hasPathSum(self, node: Optional[TreeNode], targetSum: int) -> bool:
#         if not node:
#             return
#
#         self.cur_sum += node.val
#         if not node.left and not node.right:
#             if self.cur_sum == targetSum:
#                 return True
#
#         self.hasPathSum(node.left, targetSum)
#         self.hasPathSum(node.right, targetSum)
#
#         self.cur_sum -= node.val
#
#         return False


node1 = TreeNode(1)
node2 = TreeNode(2)
node1.left = node2
print(Solution().hasPathSum(node1, 1))

