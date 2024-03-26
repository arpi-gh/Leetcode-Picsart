def majorityElement(nums: list[int]) -> int:
    # nums.sort()
    # return len(nums) // 2
    res = nums[0]
    count = 0
    for i in range(len(nums)):
        if count == 0:
            res = nums[i]
            count += 1
        elif nums[i] == res:
            count += 1
        else:
            count -= 1
    return res


ls = [3, 3, 4]
print(majorityElement(ls))
