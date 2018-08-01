#   https://leetcode.com/problems/degree-of-an-array

#   https://leetcode.com/problems/degree-of-an-array/solution


class Solution:
    #   30.02%
    def findShortesSubArray(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        d, posDict = {}, {}
        for i, n in enumerate(nums):
            if n in d:
                d[n] += 1
                posDict[n] = (min(i, posDict[n][0]), max(i, posDict[n][1]))
            else:
                d[n] = 1
                posDict[n] = (i, i)
        degree, dNums = 0, []
        for n, cnt in d.items():
            if degree < cnt:
                degree = cnt
                dNums = [n]
            elif degree == cnt:
                dNums.append(n)
        if 1 == degree:
            return 1
        minLen = len(nums)
        for n in dNums:
            minLen = min(minLen, posDict[n][1] - posDict[n][0] + 1)
        return minLen


s = Solution()
data = [([1, 2, 2, 3, 1], 2),
        ([1, 2, 2, 3, 1, 4, 2], 6),
        ([1, 2, 3, 4], 1),
        ]
for nums, expected in data:
    real = s.findShortesSubArray(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
