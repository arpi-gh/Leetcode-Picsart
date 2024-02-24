class Solution:
    def lower_bound(self, nums, target, start=0, end=None):
        if len(nums) == 0:
            return -1
        if end is None:
            end = len(nums) - 1
        mid = (start+end) // 2
        if end - start <= 1:
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            else:
                return -1
        elif nums[start] <= target <= nums[mid]:
            return Solution.lower_bound(self, nums, target, start=start, end=mid)
        elif nums[mid] <= target <= nums[end]:
            return Solution.lower_bound(self, nums, target, start=mid, end=end)
        elif target > nums[end]:
            return -1

    def upper_bound(self, nums, target, start=0, end=None):
        if len(nums) == 0:
            return -1
        if end is None:
            end = len(nums) - 1
        mid = (start+end) // 2
        if end - start <= 1:
            if nums[end] == target:
                return end
            elif nums[start] == target:
                return start
            else:
                return -1
        elif nums[mid] <= target <= nums[end]:
            return Solution.upper_bound(self, nums, target, start=mid, end=end)
        elif nums[start] <= target <= nums[mid]:
            return Solution.upper_bound(self, nums, target, start=start, end=mid)
        elif target > nums[end]:
            return -1

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first_position = Solution.lower_bound(self, nums, target)
        last_position = Solution.upper_bound(self, nums, target)
        return [first_position, last_position]


ls = [5, 5, 7, 8, 9, 9, 10, 10, 12, 12, 12, 12]
ls1 = []
ls2 = [1]
ls3 = [5, 7, 7, 8, 8, 10]
sol = Solution()
print(sol.searchRange(ls, 8))
print(sol.searchRange(ls1, 8))
print(sol.searchRange(ls3, 8))
print(sol.searchRange(ls2, 2))





