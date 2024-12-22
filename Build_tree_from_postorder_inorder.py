# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        def build(inorder, postorder, start, end, left, right):
            root = TreeNode(postorder[right])
            root_index = inorder.index(root.val)
            num_left = root_index - start
            num_right = end - root_index

            if num_left:
                root.left = build(inorder, postorder, start=start, end=root_index-1,left=left, right=left+num_left-1)
            if num_right:
                root.right = build(inorder, postorder, start=root_index+1, end=end, left=left+num_left, right=right-1)

            return root

        return build(inorder, postorder, start=0, end=len(inorder)-1, left=0, right=len(inorder)-1)


if __name__ == '__main__':
    post = [21, 15, 11, 5, 4, 3, 7, 8, 6, 20, 30]
    ino = [21, 11, 15, 30, 4, 5, 3, 20, 7, 6, 8]
    sol = Solution()
    print(sol.buildTree(ino, post))
