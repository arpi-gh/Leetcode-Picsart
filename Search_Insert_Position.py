class Solution:
    def searchInsert(self, nums: list[int], target: int, start=0, end=None) -> int:
        if len(nums) == 0:
            return start
        if end is None:
            end = len(nums) - 1
        mid = (start + end) // 2
        if target < nums[start]:
            return start
        if target > nums[end]:
            return end+1
        if end - start <= 1:
            if nums[start] == target:
                return start
            elif nums[end] == target or nums[start] < target < nums[end]:
                return end
        if nums[start] <= target <= nums[mid]:
            return Solution.searchInsert(self, nums, target, start=start, end=mid)
        if nums[mid] <= target <= nums[end]:
            return Solution.searchInsert(self, nums, target, start=mid, end=end)


ls = [5, 5, 7, 8, 9, 9, 10, 10, 12, 12, 12, 12]
ls1 = []
ls2 = [1]
ls3 = [5, 7, 7, 8, 8, 10]
sol = Solution()
print(sol.searchInsert(ls, 8))
print(sol.searchInsert(ls1, 8))
print(sol.searchInsert(ls2, 2))
print(sol.searchInsert(ls3, 11))
