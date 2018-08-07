#   https://leetcode.com/problems/relative-ranks

#   https://leetcode.com/problems/relative-ranks/discuss/98472/Python-solution


class Solution:
    #   76.82%
    def findRelativeRanks(self, nums):
        d = {}
        for i, n in enumerate(sorted(nums, reverse=True)):
            if 0 == i:
                d[n] = 'Gold Medal'
            elif 1 == i:
                d[n] = 'Silver Medal'
            elif 2 == i:
                d[n] = 'Bronze Medal'
            else:
                d[n] = str(i + 1)
        return [d[n] for n in nums]


s = Solution()
data = [([5, 4, 3, 2, 1], ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']),
        ([10, 3, 8, 9, 4], ['Gold Medal','5','Bronze Medal','Silver Medal','4']),
        ]
for nums, expected in data:
    real = s.findRelativeRanks(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
