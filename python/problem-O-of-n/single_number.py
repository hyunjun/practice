#   https://leetcode.com/problems/single-number
#   95.12%

#   https://leetcode.com/problems/single-number/solution/


from collections import Counter


class Solution:

    def singleNumber(self, nums):
        for num, count in Counter(nums).items():
            if 1 == count:
                return num
        return None


s = Solution()
data = [([2, 2, 1], 1), ([4, 1, 2, 1, 2], 4)]
for nums, expected in data:
    real = s.singleNumber(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
