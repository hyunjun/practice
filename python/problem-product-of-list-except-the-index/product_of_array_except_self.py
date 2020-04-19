#   https://leetcode.com/problems/product-of-array-except-self


from functools import reduce


class Solution:
    #   runtime; 104ms, 40.75%
    #   memory; 20.5MB, 9.07%
    def productExceptSelf0(self, nums):
        if nums is None or 0 == len(nums):
            return []
        asc = [1] * len(nums)
        dsc = [1] * len(nums)
        for i in range(1, len(nums)):
            asc[i] = nums[i - 1] * asc[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            dsc[i] = nums[i + 1] * dsc[i + 1]
        return [asc[i] * dsc[i] for i in range(len(nums))]

    #   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3300
    #   runtime; 120ms, 82.74%
    #   memory; 20.3MB
    def productExceptSelf(self, nums):
        if nums is None or 0 == len(nums):
            return []
        total, res = reduce(lambda a, b: a * b, nums), [0] * len(nums)
        for i, n in enumerate(nums):
            if 0 == n:
                res[i] = reduce(lambda a, b: a * b, nums[:i] + nums[i + 1:])
            else:
                res[i] = total // n
        return res


s = Solution()
data = [([1, 2, 3, 4], [24, 12, 8, 6]),
        ([0, 0], [0, 0]),
        ([1, 0], [0, 1]),
        ]
for nums, expected in data:
    real = s.productExceptSelf(nums)
    print(f'{nums}, expected {expected}, real {real}, result {expected == real}')
