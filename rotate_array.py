def rotate(nums: list[int], k: int) -> None:
    k = k % len(nums)
    left, right = 0, len(nums)-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    left, right = 0, k - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    left, right = k, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return


ls = [1, 2, 3, 4, 5, 6, 7]
rotate(ls, k=3)