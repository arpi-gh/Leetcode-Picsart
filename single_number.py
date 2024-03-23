def singleNumber(nums: list[int]) -> int:
    nums.sort()
    i = 0
    while i < len(nums) - 1:
        if nums[i] ^ nums[i+1] != 0:
            return nums[i]
        i += 2
    return nums[-1]


ls1 = [1, 1, 2, 2, 3]
ls2 = [1, 2, 2, 3, 3]
ls3 = [1, 1, 2, 2, 3]

print(singleNumber(ls1))
print(singleNumber(ls2))
print(singleNumber(ls3))
