#   https://leetcode.com/problems/target-sum

#   https://leetcode.com/problems/target-sum/solution


class Solution:
    #   Time Limit Exceeded
    def findTargetSumWays0(self, nums, S):
        self.cnt = 0
        def twoSums(pSum, idx):
            if idx == len(nums) - 1:
                if pSum + nums[idx] == S:
                    self.cnt += 1
                if pSum - nums[idx] == S:
                    self.cnt += 1
            else:
                twoSums(pSum + nums[idx], idx + 1)
                twoSums(pSum - nums[idx], idx + 1)
        twoSums(0, 0)
        return self.cnt

    #   Time Limit Exceeded
    def findTargetSumWays1(self, nums, S):
        res, flipIdx, isPlus = [0] * (2 ** len(nums)), 2 ** (len(nums) - 1), True
        for i, n in enumerate(nums):
            for j in range(len(res)):
                if 0 == j % flipIdx:
                    isPlus = not isPlus
                if isPlus:
                    res[j] += n
                else:
                    res[j] -= n
            flipIdx //= 2
        cnt = 0
        for r in res:
            if S == r:
                cnt += 1
        return cnt

    #   Time Limit Exceeded
    def findTargetSumWays2(self, nums, S):
        nonZeroNums = [n for n in nums if 0 < n]
        res, flipIdx, isPlus = [0] * (2 ** len(nonZeroNums)), 2 ** (len(nonZeroNums) - 1), True
        for i, n in enumerate(nonZeroNums):
            for j in range(len(res)):
                if 0 == j % flipIdx:
                    isPlus = not isPlus
                if isPlus:
                    res[j] += n
                else:
                    res[j] -= n
            flipIdx //= 2
        cnt = 0
        for r in res:
            if S == r:
                cnt += 1
        return cnt * (2 ** (len(nums) - len(nonZeroNums)))

    #   Time Limit Exceeded
    def findTargetSumWays3(self, nums, S):
        self.cnt, nonZeroNums = 0, [n for n in nums if 0 < n]
        if 0 == len(nonZeroNums):
            return 2 ** len(nums)
        def twoSums(pSum, rest, idx):
            if idx == len(nonZeroNums) - 1:
                if pSum + nonZeroNums[idx] == S:
                    self.cnt += 1
                if pSum - nonZeroNums[idx] == S:
                    self.cnt += 1
            else:
                rest -= nonZeroNums[idx]
                if pSum + nonZeroNums[idx] - rest <= S:
                    twoSums(pSum + nonZeroNums[idx], rest, idx + 1)
                if S <= pSum - nonZeroNums[idx] + rest:
                    twoSums(pSum - nonZeroNums[idx], rest, idx + 1)
        twoSums(0, sum(nonZeroNums), 0)
        return self.cnt * (2 ** (len(nums) - len(nonZeroNums)))

    #   80.83%
    def findTargetSumWays(self, nums, S):
        nonZeroNums = [n for n in nums if 0 < n]
        if 0 == len(nonZeroNums):
            return 2 ** len(nums)
        total = sum(nums)
        if total < S:
            return 0
        dps = [[0] * (total * 2 + 1) for _ in range(len(nonZeroNums))]
        for i, n in enumerate(nonZeroNums):
            if 0 == i:
                dps[0][n + total] = dps[0][-n + total] = 1
                continue
            for j, dp in enumerate(dps[i - 1]):
                if 0 < dp:
                    dps[i][j + n] += dp
                    dps[i][j - n] += dp
        return dps[-1][S + total] * (2 ** (len(nums) - len(nonZeroNums)))


s = Solution()
data = [([1, 1, 1, 1, 1], 3, 5),
        ([1, 0], 1, 2),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 1, 524288),
        ([29, 6, 7, 36, 30, 28, 35, 48, 20, 44, 40, 2, 31, 25, 6, 41, 33, 4, 35, 38], 35, 0),
        ([42, 24, 30, 14, 38, 27, 12, 29, 43, 42, 5, 18, 0, 1, 12, 44, 45, 50, 21, 47], 38, 5602),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0, 1048576), 
        ([44, 20, 38, 6, 2, 47, 18, 50, 41, 38, 32, 24, 38, 38, 30, 5, 26, 15, 37, 35], 44, 4983), 
        ([1], 2, 0),
        ]
for nums, S, expected in data:
    real = s.findTargetSumWays(nums, S)
    print('{}, {}, expected {}, real {}, result {}'.format(nums, S, expected, real, expected == real))
