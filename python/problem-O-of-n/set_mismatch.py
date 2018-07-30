#   https://leetcode.com/problems/set-mismatch

#   https://leetcode.com/problems/set-mismatch/solution


class Solution:
    #   8.33%
    def findErrorNums(self, nums):
        if nums is None or 0 == len(nums):
            return []
        d, maxVal = {}, nums[0]
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
            maxVal = max(maxVal, n)
        twice, missing = None, None
        for i in range(1, maxVal + 1):
            if 1 < d.get(i, 0):
                twice = i
            elif i not in d:
                missing = i
        if missing is None:
            missing = maxVal + 1
        return [twice, missing]


s = Solution()
data = [([1, 2, 2, 4], [2, 3]),
        ([1, 1], [1, 2])
        ]
for nums, expected in data:
    real = s.findErrorNums(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
