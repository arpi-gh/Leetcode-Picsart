class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:

        def are_similar(root1, root2):
            if (not root1 and root2) or (root1 and not root2):
                return False
            if not root1 and not root2:
                return True
            if root1.val != root2.val:
                return False
            return are_similar(root1.left, root2.left) and are_similar(root1.right, root2.right)

        if not root or not subRoot:
            return False

        if not are_similar(root, subRoot):
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        return True


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(0)

    sol = Solution()
    print(sol.isSubtree(n1, n2))
