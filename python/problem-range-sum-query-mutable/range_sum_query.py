#   https://leetcode.com/problems/range-sum-query-immutable
#   74.90%

#   https://leetcode.com/problems/range-sum-query-immutable/solution

class NumArray:

    def __init__(self, nums):
        if nums is None or 0 == len(nums):
            return
        self.nums = nums
        self.sums = [0] * len(self.nums)
        self.sums[0] = self.nums[0]
        for i in range(1, len(self.nums)):
            self.sums[i] = self.nums[i] + self.sums[i - 1]

    def sumRange(self, i, j):
        if 0 == i:
            return self.sums[j]
        return self.sums[j] - self.sums[i] + self.nums[i]


nums = [-2, 0, 3, -5, 2, -1]
na = NumArray(nums)
data = [(0, 2, 1), (2, 5, -1), (0, 5, -3)]
for i, j, expected in data:
    real = na.sumRange(i, j)
    print('{}, {}~{}, expected {}, real {}, result {}'.format(nums, i, j, expected, real, expected == real))
