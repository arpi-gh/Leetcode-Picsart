import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


# class Solution:
#     def __init__(self):
#         self.tree = []
#
#     def getHeight(self, node) -> int:
#         if not node:
#             return 0
#         left = self.getHeight(node.left)
#         right = self.getHeight(node.right)
#         return max(left, right) + 1
#
#     def dfs(self, node, height, cur_level):
#         if not node:
#             return
#         if cur_level < height:
#             if node.left:
#                 self.tree[cur_level].append(node.left.val)
#             if node.right:
#                 self.tree[cur_level].append(node.right.val)
#         self.dfs(node.left, height, cur_level=cur_level+1)
#         self.dfs(node.right, height, cur_level=cur_level+1)
#
#     def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
#         if root:
#             h = self.getHeight(root)
#             self.tree = [[] for _ in range(h)]
#             self.tree[0].append(root.val)
#             self.dfs(root, height=h, cur_level=1)
#         return self.tree


# previous solution
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
#         res = []
#         queue = collections.deque()
#         queue.append(root)
#         while queue:
#             qlen = len(queue)
#             level = []
#             for i in range(qlen):
#                 root = queue.popleft()
#                 if root:
#                     level.append(root.val)
#                     queue.append(root.left)
#                     queue.append(root.right)
#             if level:
#                 res.append(level)
#         return res


# new solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        q = [root]
        tree = []
        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                tree.append(level)

        return tree


if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    print(Solution().levelOrder(node1))