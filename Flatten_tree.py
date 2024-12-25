class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def flatten(self, root: TreeNode) -> None:
        def dfs(root):
            if not root:
                return

            elif not root.left and not root.right:
                return root

            end_of_left = dfs(root.left)
            end_of_right = dfs(root.right)
            start_of_right = root.right

            if end_of_left:
                root.right = root.left
                root.left = None
                end_of_left.right = start_of_right

            if end_of_right:
                return end_of_right
            if start_of_right:
                return start_of_right
            return end_of_left

        dfs(root)

if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t8 = TreeNode(8)
    t9 = TreeNode(9)
    t10 = TreeNode(10)
    t11 = TreeNode(11)
    t12 = TreeNode(12)

    t1.left =