#   https://leetcode.com/problems/missing-number
#   40.62%

#   https://leetcode.com/problems/missing-number/solution


class Solution:
    def missingNumber(self, nums):
        if nums is None or 0 == len(nums):
            return None
        maxNum = nums[0]
        for n in nums:
            if maxNum < n:
                maxNum = n
        allNums = list(range(maxNum + 1))
        for n in nums:
            allNums[n] = None
        for i in allNums:
            if i or 0 == i:
                return i
        return maxNum + 1



s = Solution()
data = [([0], 1), ([2], 0), ([3, 0, 1], 2), ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8)]
for nums, expected in data:
    real = s.missingNumber(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
