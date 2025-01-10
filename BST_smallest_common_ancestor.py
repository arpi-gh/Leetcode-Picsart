# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def __init__(self):
        self.left = False
        self.right = False
        self.lca = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = root

        def dfs(root, child1=p, child2=q):
            if not root:
                return

            dfs(root.left, p, q)
            dfs(root.right, p, q)

            if root == child1 or root == child2:
                if not self.left:
                    self.left = True
                else:
                    self.right = True

            if self.left and self.right and root.val < self.lca.val:
                self.lca = root

        dfs(root, p, q)

        return self.lca


if __name__ == '__main__':
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n8 = TreeNode(8)
    n0 = TreeNode(0)
    n4 = TreeNode(4)
    n7 = TreeNode(7)
    n9 = TreeNode(9)
    n3 = TreeNode(3)
    n5 = TreeNode(5)

    n6.left = n2
    n6.right = n8
    n2.left = n0
    n2.right = n4
    n4.left = n3
    n4.right = n5
    n8.left = n7
    n8.right = n9

    sol = Solution()
    print(sol.lowestCommonAncestor(n6, p=n2, q=n4))
