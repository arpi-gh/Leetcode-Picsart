def removeDuplicates(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    prev = nums[0]
    count = 1
    i = 1
    while i != len(nums):
        if nums[i] == prev:
            count += 1
        else:
            count = 1
            prev = nums[i]
        if count > 2:
            nums.pop(i)
        else:
            i += 1
    k = len(nums)
    return k


ls = [0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 6]
print(removeDuplicates(ls))
