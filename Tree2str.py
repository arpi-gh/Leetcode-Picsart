class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def tree2str(self, root: TreeNode) -> str:
        res = ''

        def dfs(root):
            nonlocal res
            if not root:
                return

            res += f'{root.val}'
            if not root.left and not root.right:
                return

            if root.left:
                res += '('
                dfs(root.left)
                res += ')'
            if root.right:
                if not root.left:
                    res += '()'
                res += '('
                dfs(root.right)
                res += ')'

        dfs(root)
        return res


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    sol = Solution()
    print(sol.tree2str(n1))
