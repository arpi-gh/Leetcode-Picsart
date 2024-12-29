# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# bfs solution

# class Solution:
#     def rightSideView(self, root: TreeNode) -> list[int]:
#         if not root:
#             return []
#
#         res = []
#
#         def bfs(root):
#             q = [root]
#             while q:
#                 res.append(q[-1].val)
#                 for i in range(len(q)):
#                     node = q.pop(0)
#                     if node.left:
#                         q.append(node.left)
#                     if node.right:
#                         q.append(node.right)
#
#         bfs(root)
#         return res

# dfs solution

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        res = []

        def dfs(root, level=0):
            if not root:
                return
            if len(res) < level + 1:
                res.append(root.val)
            else:
                res[level] = root.val

            dfs(root.left, level=level + 1)
            dfs(root.right, level=level + 1)

        dfs(root)
        return res

