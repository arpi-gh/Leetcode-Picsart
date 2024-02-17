class Solution:
    @staticmethod
    def two_sum_1(nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

    @staticmethod
    def two_sum_2(nums, target):
        addends = {}
        for i in range(len(nums)):
            addend = target - nums[i]
            if addend in addends.keys():
                return addends[addend], i
            addends[nums[i]] = i


if __name__ == '__main__':
    inp = input('Enter a list of numbers: ')
    num_list = []
    for item in inp:
        if item.isdigit():
            num_list.append(int(item))
    target_num = int(input('Enter the target number: '))
    solution_1 = Solution().two_sum_1(num_list, target_num)
    solution_2 = Solution().two_sum_2(num_list, target_num)
    print('O(n^2) solution: ', solution_1)
    print('O(n) solution: ', solution_2)