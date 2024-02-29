def removeDuplicates(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    largest = max(nums) + 100
    i = 0
    count = 1
    while i < len(nums)-1:
        j = i + 1
        while j < len(nums):
            if not nums[i] ^ nums[j]:   # If the numbers are the same
                nums[j] = largest
                j += 1
                if j == len(nums):
                    i = j
            else:
                i = j
                count += 1
                break
    nums.sort()
    return count


numbers = [1, 1, 2]
numbers1 = []
numbers2 = [2]
numbers3 = [1, 1, 2, 3, 4, 5, 5, 5]
print(removeDuplicates(numbers))
numbers.sort()
print(numbers)
# print(removeDuplicates(numbers1))
# numbers1.sort()
# print(numbers1)
# print(removeDuplicates(numbers2))
# numbers2.sort()
# print(numbers2)
# print(removeDuplicates(numbers3))
# numbers3.sort()
# print(numbers3)

