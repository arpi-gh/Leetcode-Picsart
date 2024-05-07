from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def __init__(self):
#         self.x = 1
#
#     def dfs(self, node) -> int:
#         if node is None:
#             return 0
#
#         left = self.dfs(node.left)
#         right = self.dfs(node.right)
#
#         if node.left is None and node.right is None:
#             self.x = 1
#         else:
#             self.x += 1
#
#         return (node.val * 10 ** self.x) + left + right
#
#     def sumNumbers(self, node: Optional[TreeNode]) -> int:
#         dummy = TreeNode(0)  # 0
#         dummy.left = TreeNode(node.val)  # 0 -> 4
#         dummy.right = TreeNode(node.val)  # 0 -> 4
#         dummy.left.left = node.left  # 0 -> 4 -> 9 -> 5 / 0 -> 4 -> 9-> 1
#         node.left = None
#         dummy.right.right = node.right  # 0 -> 4 -> 0
#
#         return self.dfs(dummy)


class Solution:
    def __init__(self):
        self.nums = []

    def extract(self, node, cur_num=''):
        if node is None:
            return

        cur_num += str(node.val)
        if not node.left and not node.right:
            self.nums.append(int(cur_num))

        self.extract(node.left, cur_num)
        self.extract(node.right, cur_num)

        cur_num = cur_num[:-1]

        return

    def sumNumbers(self, node: Optional[TreeNode]) -> int:
        res = 0
        self.extract(node)
        for num in self.nums:
            res += num
        return res

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
