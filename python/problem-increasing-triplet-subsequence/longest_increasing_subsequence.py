#   https://leetcode.com/problems/longest-increasing-subsequence

#   https://leetcode.com/problems/longest-increasing-subsequence/solution


class Solution:
    #   Wrong Answer
    def lengthOfLIS0(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        if 1 == len(nums):
            return 1
        sortedNums = sorted([(i, n) for i, n in enumerate(nums)], key=lambda t: t[1])
        res = 0
        for i, (idx, n) in enumerate(sortedNums):
            prevIdx, prevNum, lisCnt = idx, n, 1
            for j in range(i + 1, len(nums)):
                if prevIdx < sortedNums[j][0] and prevNum < sortedNums[j][1]:
                    prevIdx = sortedNums[j][0]
                    prevNum = sortedNums[j][1]
                    lisCnt += 1
            res = max(res, lisCnt)
        return res

    #   Wrong Answer
    def lengthOfLIS1(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        if 1 == len(nums):
            return 1
        lisList = [[] for _ in range(len(nums))]
        for i, n in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if nums[j] <= n:
                    continue
                if 0 == len(lisList[j]):
                    lisList[j].append(n)
                else:
                    if n < lisList[j][-1]:
                        lisList[j][-1] = n
                    else:
                        lisList[j].append(n)
        res = 0
        for lis in lisList:
            res = max(res, len(lis) + 1)
        return res

    #   6.98%
    def lengthOfLIS(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        if 1 == len(nums):
            return 1
        res = [0] * len(nums)
        for i, n in enumerate(nums):
            for j in range(i - 1, -1, -1):
                if nums[j] < n:
                    res[i] = max(res[i], res[j] + 1)
        return max(res) + 1


s = Solution()
data = [([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
        ([4, 10, 4, 3, 8, 9], 3),
        ]
for nums, expected in data:
    real = s.lengthOfLIS(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
