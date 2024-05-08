class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = None

    def dfs(self, node, node1, node2):

        if node is None:
            return

        left = self.dfs(node.left, node1, node2)
        right = self.dfs(node.right, node1, node2)

        if node.val == node1.val or node.val == node2.val:
            return node

        if left and right:
            return node
        elif left:
            return left
        elif right:
            return right

        return

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        return self.dfs(root, p, q)