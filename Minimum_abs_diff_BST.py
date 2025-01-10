class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        min_diff = 10 ** 6
        prev_num = None

        def dfs(root):
            nonlocal min_diff
            nonlocal prev_num

            if not root:
                return

            dfs(root.left)

            cur_num = root.val
            if prev_num is not None:
                cur_diff = cur_num - prev_num
                if cur_diff < min_diff:
                    min_diff = cur_diff
            prev_num = cur_num

            dfs(root.right)

        dfs(root)
        return min_diff


if __name__ == '__main__':
    n1 = TreeNode(0)
    n2 = TreeNode(2236)
    n3 = TreeNode(1277)
    n4 = TreeNode(2776)
    n5 = TreeNode(519)

    n1.right = n2
    n2.left = n3
    n2.right = n4
    n3.left = n5

    sol = Solution()
    print(sol.getMinimumDifference(n1))