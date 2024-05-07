from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def __init__(self):
#         self.nums = []
#
#     def extract(self, node, cur_num=''):
#         if node is None:
#             return
#
#         cur_num += str(node.val)
#         if not node.left and not node.right:
#             self.nums.append(int(cur_num))
#
#         self.extract(node.left, cur_num)
#         self.extract(node.right, cur_num)
#
#         cur_num = cur_num[:-1]
#
#         return
#
#     def sumNumbers(self, node: Optional[TreeNode]) -> int:
#         res = 0
#         self.extract(node)
#         for num in self.nums:
#             res += num
#         return res

class Solution:
    def __init__(self):
        self.sum = 0
    def sumNumbers(self, node: Optional[TreeNode], num=0) -> int:
        if not node:
            return

        num = num * 10 + node.val

        if not node.left and not node.right:
            self.sum += num
            num //= 10

        self.sumNumbers(node.left, num)
        self.sumNumbers(node.right, num)

        return self.sum


node4 = TreeNode(4)
node9 = TreeNode(9)
node5 = TreeNode(5)
node1 = TreeNode(1)
node0 = TreeNode(0)

node4.left = node9
node4.right = node0
node9.left = node5
node9.right = node1

#    0
#   4
#  9
# 5 1

print(Solution().sumNumbers(node4))
