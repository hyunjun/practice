#   https://leetcode.com/problems/product-of-array-except-self


class Solution:
    #   runtime; 104ms, 40.75%
    #   memory; 20.5MB, 9.07%
    def productExceptSelf(self, nums):
        if nums is None or 0 == len(nums):
            return []
        asc = [1] * len(nums)
        dsc = [1] * len(nums)
        for i in range(1, len(nums)):
            asc[i] = nums[i - 1] * asc[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            dsc[i] = nums[i + 1] * dsc[i + 1]
        return [asc[i] * dsc[i] for i in range(len(nums))]


s = Solution()
data = [([1, 2, 3, 4], [24, 12, 8, 6]),
        ]
for nums, expected in data:
    real = s.productExceptSelf(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
