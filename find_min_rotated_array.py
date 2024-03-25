def findMin(nums: list[int], start=0, end=None) -> int:
    if end is None:
        end = len(nums) - 1
        if nums[start] < nums[end]:
            return nums[start]
    mid = (start+end) // 2
    if start == mid:
        return min(nums[start], nums[end])
    if nums[mid] < nums[end]:
        if nums[start] <= nums[mid-1]:
            return nums[mid]
        else:
            return findMin(nums,start=start, end=mid)
    elif nums[mid] > nums[end]:
        return findMin(nums, start=mid, end=end)