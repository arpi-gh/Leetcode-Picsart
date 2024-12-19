from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'

# Previous solution

# class Solution:
#     @staticmethod
#     def dfs(node1, node2) -> bool:
#         if not node1 and not node2:
#             return True
#         elif not node1 or not node2:
#             return False
#         elif node1.val != node2.val:
#             return False
#
#         return Solution().dfs(node1.left, node2.right) and Solution().dfs(node1.right, node2.left)
#
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         return Solution().dfs(root.left, root.right)

# New Solution
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(root1, root2) -> bool:
            if not root1 and not root2:
                return True
            if (root1 and not root2) or (root2 and not root2):
                return False
            if root1.val != root2.val:
                return False

            return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)

        return dfs(root.left, root.right)


if __name__ == '__main__':
    # Creating the nodes
    root = TreeNode(1)
    node2_left = TreeNode(2)
    node2_right = TreeNode(2)
    node3_left = TreeNode(3)
    node4_left = TreeNode(4)
    node4_right = TreeNode(4)
    node3_right = TreeNode(3)

    # Connecting the nodes
    root.left = node2_left
    root.right = node2_right
    node2_left.left = node3_left
    node2_left.right = node4_left
    node2_right.left = node4_right
    node2_right.right = node3_right

    sol = Solution()
    print(sol.isSymmetric(root))
