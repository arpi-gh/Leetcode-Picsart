from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int], start=0, end=None) -> Optional[TreeNode]:
        if end is None:
            end = len(nums) - 1
        if end - start < 0:
            return
        mid = (start + end) // 2
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums, start=start, end=mid-1)
        root.right = self.sortedArrayToBST(nums, start=mid+1, end=end)

        return root


ls = [8, 10, 11, 15, 16, 17, 18, 20, 21, 22, 23, 25, 30, 35]
r = Solution().sortedArrayToBST(ls)
print(r.val)


