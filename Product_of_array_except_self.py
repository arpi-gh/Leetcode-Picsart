class Solution(object):
    # O(n**2) solution
    # def productExceptSelf(self, nums):
    #     products = [0] * len(nums)
    #     for i in range(len(nums)):
    #         product = 1
    #         for j in range(len(nums)):
    #             if i != j:
    #                 product *= nums[j]
    #         products[i] = product
    #     return products
    def productExceptSelf(self, nums):
        end = len(nums) - 1
        prefix = {0: 1}
        suffix = {end: 1}
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
            j = end-i
            suffix[j] = suffix[j+1] * nums[j+1]
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        return res


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    sol = Solution()
    print(sol.productExceptSelf(arr))

