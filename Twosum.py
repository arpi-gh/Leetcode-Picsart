# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]


class Solution:
    def twoSum(self, nums, target):
        addends = {}
        for i in range(len(nums)):
            addend = target - nums[i]
            if addend in addends.keys():
                return addends[addend], i
            addends[nums[i]] = i


if __name__ == '__main__':
    inp = input()
    num_list = []
    for item in inp:
        if item.isdigit():
            num_list.append(int(item))
    target_num = int(input())
    solution = Solution().twoSum(num_list, target_num)
    print(solution)
