#   https://leetcode.com/problems/minimum-cost-tree-from-leaf-values


from typing import List


class Solution:
    #   Wrong Answer
    def mctFromLeafValues0(self, arr: List[int]) -> int:
        if arr is None or not (2 <= len(arr) <= 40):
            return 0

        tot, arr = 0, [[a, a] for a in sorted(arr)]
        while 1 < len(arr):
            for i in range(1, len(arr), 2):
                arr[i - 1][0], arr[i - 1][1] = arr[i - 1][1] * arr[i][1], arr[i][1]
                tot += arr[i - 1][0]
                arr[i] = None
            arr = [a for a in arr if a]
        return tot

    #   Time Limit Exceeded
    def mctFromLeafValues1(self, arr: List[int]) -> int:
        if arr is None or not (2 <= len(arr) <= 40):
            return 0

        def getMinSum(nums):
            if 1 == len(nums):
                return [0, nums[0]]
            if 2 == len(nums):
                return [nums[0] * nums[1], max(nums[0], nums[1])]
            minRes = [float('inf'), 0]
            for i in range(1, len(nums)):
                x, y = getMinSum(nums[:i]), getMinSum(nums[i:])
                curSum = x[1] * y[1] + x[0] + y[0]
                if curSum < minRes[0]:
                    minRes = [curSum, max(x[1], y[1])]
            return minRes

        return getMinSum(arr)[0]

    #   runtime; 1048ms, 5.33%
    #   memory; 14.1MB, 100.00%
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if arr is None or not (2 <= len(arr) <= 40):
            return 0

        self.memo = {}
        def getMinSum(nums):
            key = ' '.join(str(n) for n in nums)
            if key in self.memo:
                return self.memo[key]
            if 1 == len(nums):
                return [0, nums[0]]
            if 2 == len(nums):
                return [nums[0] * nums[1], max(nums[0], nums[1])]
            minRes = [float('inf'), 0]
            for i in range(1, len(nums)):
                x, y = getMinSum(nums[:i]), getMinSum(nums[i:])
                curSum = x[1] * y[1] + x[0] + y[0]
                if curSum < minRes[0]:
                    minRes = [curSum, max(x[1], y[1])]
            self.memo[key] = minRes
            return minRes

        return getMinSum(arr)[0]


s = Solution()
data = [([6, 2, 4], 32),
        ([6, 2, 4, 5], 58),
        ([6, 2, 4, 5, 1, 3, 9], 130),
        ([10,7,15,12,13,12,14,1,3,14,3,12,14,2,5], 1645),
        ]
for arr, expected in data:
    real = s.mctFromLeafValues(arr)
    print(f'{arr}, expected {expected}, real {real}, result {expected == real}')
