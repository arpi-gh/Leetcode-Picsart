def maxSubArray(nums: list[int]) -> int:
    max_sum = max(nums)
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum < 0:
            current_sum = 0
        elif current_sum > max_sum:
            max_sum = current_sum
    return max_sum
