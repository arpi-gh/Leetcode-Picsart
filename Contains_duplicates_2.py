class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        numbers = {}
        for i in range(len(nums)):
            if nums[i] in numbers:
                if i - numbers[nums[i]] <= k:
                    return True
            numbers[nums[i]] = i
        return False