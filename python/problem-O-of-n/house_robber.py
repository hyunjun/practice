#   https://leetcode.com/problems/house-robber

#   https://leetcode.com/problems/house-robber/discuss/55696/Python-solution-3-lines.


from typing import List


class Solution:
    #   runtime; 52ms, 21.86%
    def rob0(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        maximized = 0
        for i, n in enumerate(nums):
            if 2 < i:
                nums[i] += max(nums[i - 2], nums[i - 3])
            elif 1 < i:
                nums[i] += nums[i - 2]
            if maximized < nums[i]:
                maximized = nums[i]
        return maximized

    #   https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3459
    #   Time Limit Exceeded
    def rob1(self, nums: List[int]) -> int:
        
        def getSum(acc, i):
            if len(nums) <= i:
                return acc
            return max(getSum(acc + nums[i], i + 2), getSum(acc + nums[i], i + 3))
        
        return max(getSum(0, 0), getSum(0, 1))

    #   runtime; 48ms, 16.71%
    #   memory; 13.7MB, 81.44%
    def rob(self, nums: List[int]) -> int:
        res = 0
        for i, n in enumerate(nums):
            if 0 <= i - 3:
                nums[i] += max(nums[i - 2], nums[i - 3])
            elif 0 <= i - 2:
                nums[i] += nums[i - 2]
            res = max(res, nums[i])
        return res


s = Solution()
data = [([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([13, 1, 1, 4, 2], 17),
        ([2, 1, 1, 2], 4),
        ([226,174,214,16,218,48,153,131,128,17,157,142,88,43,37,157,43,221,191,68,206,23,225,82,54,118,111,46,80,49,245,63,25,194,72,80,143,55,209,18,55,122,65,66,177,101,63,201,172,130,103,225,142,46,86,185,62,138,212,192,125,77,223,188,99,228,90,25,193,211,84,239,119,234,85,83,123,120,131,203,219,10,82,35,120,180,249,106,37,169,225,54,103,55,166,124], 7102),
        ]
for nums, expected in data:
    real = s.rob(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
