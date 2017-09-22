#   https://leetcode.com/problems/product-of-array-except-self
#   56.10%

class Solution:
    def productExceptSelf(self, nums):
        if nums is None or 0 == len(nums):
            return []
        tot_len = len(nums)
        acc, prod = 1, [1] * tot_len
        for i in range(1, tot_len):
            acc *= nums[i - 1]
            prod[i] *= acc
        acc = 1
        for i in range(tot_len - 2, -1, -1):
            acc *= nums[i + 1]
            prod[i] *= acc
        return prod

s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
