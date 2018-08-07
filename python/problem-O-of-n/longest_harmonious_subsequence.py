#   https://leetcode.com/problems/longest-harmonious-subsequence

#   https://leetcode.com/problems/longest-harmonious-subsequence/solution


class Solution:
    #   55.60%
    def findLHS(self, nums):
        d = {}
        for i, n in enumerate(nums):
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        maxLen = 0
        for n, cnt in d.items():
            if n - 1 in d:
                maxLen = max(maxLen, cnt + d[n - 1])
            if n + 1 in d:
                maxLen = max(maxLen, cnt + d[n + 1])
        return maxLen


s = Solution()
data = [([1, 3, 2, 2, 5, 2, 3, 7], 5),
        ]
for nums, expected in data:
    real = s.findLHS(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
