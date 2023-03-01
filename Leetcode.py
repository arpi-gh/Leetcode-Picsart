class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# inp = input()
# num_list = []
# for item in inp:
#     if item.isdigit():
#         num_list.append(int(item))
# target_num = int(input())
# solution = Solution().twoSum(num_list, target_num)
# print(solution)




def maxProfit(prices) :
    max_profit = 0
    for i in range(len(prices)-1, -1, -1):
        for j in range(i):
            if prices[i] - prices[j] > max_profit:
                max_profit = prices[i] - prices[j]
    return max_profit


# ls = [7, 1, 5, 3, 6, 4]
# prof = maxProfit(ls)
# print(ls)
# print(prof)



def containsDuplicate(nums):
    num_set = set(nums)
    if len(num_set) < len(nums):
        return True
    else:
        return False
    # dupl = False   # not optimal
    # unique_ls = []
    # for i in range(len(nums)):
    #     if nums[i] not in unique_ls:
    #         unique_ls.append(nums[i])
    #     else:
    #         dupl = True
    #         break
    # return dupl

# ls = [1,2,3,1]
# print(containsDuplicate(ls))


'''Given two integers a and b, return the sum of the two integers without using the operators + and -.
Կյանքը բարդացնելու համար կոդ․ բինար գումարում xor-ի և and-ի միջոցով - աշխատում է միայն դրական թվերի համար'''

'''
a = int(input('a = '))
b = int(input('b = '))
bin_a = bin(a)[2:]
bin_b = bin(b)[2:]
len_dif = len(bin_a) - len(bin_b)
_sum = []
if len_dif < 0:
    len_dif = abs(len_dif)
    a_l = [0] * (len_dif+1)
    a_l.extend([int(n) for n in bin_a])
    b_l = [0]
    b_l.extend([int(m) for m in bin_b])
else:
    a_l = [0]
    a_l.extend([int(n) for n in bin_a])
    b_l = [0] * (len_dif+1)
    b_l.extend([int(m) for m in bin_b])
carry = 0
for i in range(len(a_l)-1, -1,-1):
    _sum.append(carry ^ a_l[i] ^ b_l[i])
    carry = (carry | a_l[i]) & b_l[i]
final_num = 0
for i in range(len(_sum)):
    final_num += _sum[i] * (2 ** i)
print(final_num)'''


def hammingWeight(n) -> int:
    n = bin(n)
    n = n[2:]
    counter = 0
    for digit in n:
        if digit == '1':
            counter += 1
    return counter


'''num = int(input(), 2)
print(hammingWeight(num))'''


def reverseBits(n):
    n = '{:032b}'.format(n)
    n = n[::-1]
    new_n = '0b' + n
    new_n = int(new_n, 2)
    return new_n


'''num = str(input('num: '))
print(reverseBits(num)'''


# [-2, 1, -20, 4, -1, 2, 1, -21, 4]


'''doesn't work when there are too many negative numbers (( The algorithm needs to be modified a little'''


def maxSubArray(nums):
    min_num = min(nums)
    _slice = nums.index(min_num)
    whole_sum = sum(nums)
    if len(nums) != 0:
        if min_num > 0:
            return nums
    left = nums[0:_slice]
    right = nums[_slice + 1:]
    if sum(left) > whole_sum or sum(right) > whole_sum:
        if sum(left) > sum(right):
            nums = nums[0:_slice]
        else:
            nums = nums[_slice + 1:]
        return maxSubArray(nums)
    else:
        return nums


ls = [-2, 1, -20, 4, -1, 2, 1, -21, 4]
print(maxSubArray(ls))