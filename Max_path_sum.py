# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def __init__(self):
        self.max_sum = 0

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = root.val

        def count(root):
            if not root:
                return 0

            left = max(count(root.left), 0)
            right = max(count(root.right), 0)

            self.max_sum = max((left + right + root.val), self.max_sum)
            return max(left, right) + root.val
        counted = count(root)
        return max(self.max_sum, counted)


if __name__ == '__main__':
    n1 = TreeNode(-10)
    n2 = TreeNode(9)
    n3 = TreeNode(20)
    n4 = TreeNode(15)
    n5 = TreeNode(7)

    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5

    sol = Solution()
    print(sol.maxPathSum(n1))
