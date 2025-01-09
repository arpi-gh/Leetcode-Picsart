from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'

# class Solution:
#     def __init__(self):
#         self.res = []
#         self.count = 0
#         self.max_count = 0
#         self.prev = None
#
#     def dfs(self, node):
#         if not node:
#             return
#
#         self.dfs(node.left)
#
#         if self.prev is None:
#             self.prev = node.val
#
#         if node.val == self.prev:
#             self.count += 1
#         else:
#             self.count = 1
#
#         if self.count > self.max_count:
#             self.res = []
#             self.res.append(node.val)
#             self.max_count = self.count
#         elif self.count == self.max_count:
#             self.res.append(node.val)
#
#         self.prev = node.val
#
#         self.dfs(node.right)
#
#         return
#
#     def findMode(self, root: Optional[TreeNode]) -> List[int]:
#         self.dfs(root)
#         return self.res


class Solution:
    def __init__(self):
        self.prev_num = -(10**6)
        self.cur_num = 0
        self.max_count = 0
        self.cur_count = 0
        self.result = []

    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def check_and_update():
            if self.cur_count > self.max_count:
                self.result = [self.prev_num]
                self.max_count = self.cur_count
            elif self.max_count and self.cur_count == self.max_count:
                self.result.append(self.prev_num)

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            self.cur_num = root.val
            if self.cur_num != self.prev_num:
                check_and_update()
                self.prev_num = self.cur_num
                self.cur_count = 1
            elif self.cur_num == self.prev_num:
                self.cur_count += 1
            dfs(root.right)

        dfs(root)
        check_and_update()
        return self.result


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(2)
    n1.right = n2
    n2.right = n3
    sol = Solution()
    print(sol.findMode(n1))
