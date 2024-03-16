def sortColors(nums: list[int]) -> None:
    colors = [0, 0, 0]
    for num in nums:
        colors[num] += 1
    colors[1] += colors[0]
    colors[2] += colors[1]
    num = 0
    j = 0
    while num <= 2:
        while j != colors[num]:
            nums[j] = num
            j += 1
        num += 1


user_input = [2, 0, 2, 1, 1, 0]
sortColors(user_input)


