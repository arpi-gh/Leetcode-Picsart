class Solution:
    def search(self, nums: list[int], target: int, start=0, end=None) -> int:
        if end is None:
            end = len(nums)-1
        mid = ((start+end) // 2)
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        elif start == mid:
            return -1
        elif nums[start] < nums[end]:
            if target >= nums[mid]:
                return Solution.search(self, nums, target, start=mid, end=end)
            else:
                return Solution.search(self, nums, target, start=start, end=mid)
        elif nums[mid] < nums[end]:
            if nums[mid] <= target <= nums[end]:
                return Solution.search(self, nums, target, start=mid, end=end)
            else:
                return Solution.search(self, nums, target, start=start, end=mid)
        else:
            if nums[start] <= target <= nums[mid]:
                return Solution.search(self, nums, target, start=start, end=mid)
            else:
                return Solution.search(self, nums, target, start=mid, end=end)


ls1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ls2 = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
ls3 = [3, 4, 5, 6, 7, 0, 1, 2]
ls4 = [1, 3]
ls5 = [5, 1, 3]
ls6 = [4, 5, 6, 7, 8, 1, 2, 3]
sol = Solution()

print(sol.search(ls1, 4))
print(sol.search(ls2, 5))
print(sol.search(ls3, 0))
print(sol.search(ls4, 2))
print(sol.search(ls5, 5))
print(sol.search(ls6, 8))


