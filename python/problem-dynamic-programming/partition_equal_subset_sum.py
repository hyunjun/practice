#   https://leetcode.com/problems/partition-equal-subset-sum

#   https://medium.freecodecamp.org/a-variation-on-the-knapsack-problem-how-to-solve-the-partition-equal-subset-sum-problem-in-java-7e0fc047f19b
#   https://leetcode.com/problems/partition-equal-subset-sum/discuss/286594/python-dynamic-programming


class Solution:
    #   Wrong Answer
    def canPartition0(self, nums):
        if nums is None or 0 == len(nums):
            return False
        target = sum(nums)
        if target % 2 != 0:
            return False
        target //= 2
        nums.sort()
        dp = [False] * (target + 1)
        dp[0] = True
        for i in range(1, len(dp)):
            for n in nums:
                if i < n:
                    continue
                dp[i] = dp[i - n]
        return dp[-1]

    #   Time Limit Exceeded
    def canPartition1(self, nums):
        if nums is None or 0 == len(nums):
            return False
        target = sum(nums)
        if target % 2 != 0:
            return False
        target //= 2
        nums.sort()

        self.d = {}
        def hasEqualTarget(prev, arr):
            key, curSum = ''.join([str(p) for p in prev]), sum(prev)
            if key in self.d:
                return self.d[key]
            if target == curSum:
                self.d[key] = True
                return True
            if target < curSum:
                self.d[key] = False
                return False
            for i, a in enumerate(arr):
                prev.append(a)
                if hasEqualTarget(prev, arr[:i] + arr[i + 1:]):
                    return True
                prev.pop()
            self.d[key] = False
            return False

        return hasEqualTarget([], nums)

    #   개수가 많지 않은 경우는 dict를 이용한 memoization이 없는 게 오히려 빠름
    def canPartition2(self, nums):
        if nums is None or 0 == len(nums):
            return False
        target = sum(nums)
        if target % 2 != 0:
            return False
        target //= 2
        nums.sort()

        def hasEqualTarget(prev, arr):
            curSum = sum(prev)
            if target == curSum:
                return True
            if target < curSum:
                return False
            for i, a in enumerate(arr):
                prev.append(a)
                if hasEqualTarget(prev, arr[:i] + arr[i + 1:]):
                    return True
                prev.pop()
            return False

        return hasEqualTarget([], nums)

    #   runtime; 552ms, 59.48%
    #   memory; 13.2MB, 42.73%
    def canPartition(self, nums):
        if nums is None or 0 == len(nums):
            return False
        numSum = sum(nums)
        if numSum % 2 != 0:
            return False
        target  = numSum // 2
        nums.sort()

        dp = [False] * (numSum + 1)
        dp[0] = True
        for num in nums:
            for i in range(numSum, -1, -1):
                if dp[i]:
                    dp[num + i] = True
            if dp[target]:
                return True
        return False


s = Solution()
data = [([1, 5, 11, 5], True),
        ([1, 2, 3, 5], False),
        ([1, 2, 5], False),
        ([80,38,97,19,81,96,70,35,12,44,33,51,78,86,31,74,94,54,11,91,7,90,83,12,91,67,40,80,39,87,17,49,66,56,15,99,95,91,22,49,14,23,18,74,22,62,14,94,75,97,45,32,9,21,14,70,93,14,91,6,99,12,29,32,26,33,44,24,82,84,95,10,91,38,23,27,64,88,83,85,7,23,62,49,60,67,31,55,87,42,61,4,7,10,12,8,94,9,30,59], True),
        ]
for nums, expected in data:
    real = s.canPartition(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
