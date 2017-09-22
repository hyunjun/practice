#   https://leetcode.com/problems/increasing-triplet-subsequence
#   brute force O(n^3)
#   O(n^2) also easy
#   O(nlogn) (sort) easiest

#   https://discuss.leetcode.com/topic/39807/python-easy-o-n-solution/4
#   판정기 이상. index가 i < j < k가 아닌데도 정상 판정 준 듯

#   64.68%


import sys

class Solution:
    def increasingTriplet(self, nums):
        if nums is None or len(nums) < 3:
            return False

        first = second = sys.maxsize
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                print('{} < {} < {}'.format(first, second, n))
                return True

        return False


s = Solution()
cases = [([1, 2, 3, 4, 5], True),
         ([5, 4, 3, 2, 1], False), ([0, 1], False),
         ([5, 1, 2, 2, 3, 4, -1], True), ([5, 1, 5, 5, 2, 5, 4], True),
         ([5, 1, 5, 5, 2, -1, 4], True), ([2, 1, 5, 3, 4], True), ([1, 2, 3, 1, 2, 1], True),
         #([1,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100000000], True)
        ]
for nums, expected in cases:
    print()
    real = s.increasingTriplet(nums)
    print('{}\texpected {}\treal {}\tresult {}'.format(nums, expected, real, expected == real))
