from math import inf
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def __init__(self):
        self.ls = []
        self.index = 0

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.ls.append(root.val)
        self.dfs(root.right)

    def replace(self, root):
        if not root:
            return
        self.replace(root.left)
        root.val = self.ls[self.index]
        self.index += 1
        self.replace(root.right)

    def recoverBST(self, root):
        self.dfs(root)
        self.ls.sort()
        print(self.ls)
        self.replace(root)
        return root


if __name__ == '__main__':
    n1 = TreeNode(20)
    n2 = TreeNode(10)
    n3 = TreeNode(30)
    n4 = TreeNode(5)
    n5 = TreeNode(25)
    n6 = TreeNode(15)
    n7 = TreeNode(35)
    n8 = TreeNode(1)
    n9 = TreeNode(7)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n4.right = n9

    sol = Solution()
    print(sol.recoverBST(n1))
