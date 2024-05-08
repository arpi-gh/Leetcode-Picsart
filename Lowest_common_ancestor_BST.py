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

        self.dfs(node.left, node1, node2)
        self.dfs(node.right, node1, node2)

        if node1.val <= node.val <= node2.val:
            self.res = node

        return self.res

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < q.val:
            node_1, node_2 = p, q
        else:
            node_1, node_2 = q, p

        return self.dfs(root, node_1, node_2)


n6 = TreeNode(6)
n2 = TreeNode(2)
n8 = TreeNode(8)
n0 = TreeNode(0)
n4 = TreeNode(4)
n7 = TreeNode(7)
n9 = TreeNode(9)

n6.left = n2
n6.right = n8
n2.left = n0
n2.right = n4
n8.left = n7
n8.right = n9

print(Solution().lowestCommonAncestor(n6, TreeNode(2), TreeNode(4)))