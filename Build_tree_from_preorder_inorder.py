class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]):
        visited = [False] * len(preorder)
        nodes = {val: None for val in preorder}
        root = TreeNode(preorder[0])
        nodes[preorder[0]] = root
        edge = inorder.index(preorder[0])
        visited[edge] = True

        for val in preorder[1:]:
            node = TreeNode(val)
            index = inorder.index(val)
            if edge > index:
                for i in range(index, edge + 1):
                    if visited[i]:
                        nodes[inorder[i]].left = node
                        break

            elif edge < index:
                for i in range(index, edge - 1, -1):
                    if visited[i]:
                        nodes[inorder[i]].right = node
                        break

            nodes[val] = node
            visited[index] = True
            edge = index

        return root


if __name__ == '__main__':
    sol = Solution()
    pre = [3, 9, 20, 15, 7]
    ino = [9, 3, 15, 20, 7]
    print(sol.buildTree(pre, ino))
