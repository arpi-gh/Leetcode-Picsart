from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.cur_sum = 0
        self.sums = []
        self.path = []

    def dfs(self, node, target_sum):
        if not node:
            return

        self.cur_sum += node.val
        self.path.append(node.val)
        if not node.left and not node.right:
            if self.cur_sum == target_sum:
                tmp = self.path.copy()
                self.sums.append(tmp)

        self.dfs(node.left, target_sum)
        self.dfs(node.right, target_sum)

        self.cur_sum -= node.val
        self.path.pop()

        return

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        self.dfs(root, targetSum)
        return self.sums


n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(8)
n4 = TreeNode(11)
n5 = TreeNode(2)
n6 = TreeNode(13)
n7 = TreeNode(4)
n8 = TreeNode(5)

n1.left = n2
n1.right = n3
n2.left = n4
n3.left = n6
n3.right = n2
n4.right = n5
n2.right = n8

Solution().pathSum(n1, 22)
print(Solution().sums)