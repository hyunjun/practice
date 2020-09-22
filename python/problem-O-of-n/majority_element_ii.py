#   https://leetcode.com/problems/majority-element-ii

#   https://leetcode.com/problems/majority-element-ii/solution


from collections import Counter
from typing import List


class Solution:
    #   https://leetcode.com/explore/featured/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3469/
    #   runtime; 208ms, 8.52%
    #   memory; 14.9MB, 77.86%
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [n for n, cnt in Counter(nums).items() if cnt > len(nums) / 3]


s = Solution()
data = [([3, 2, 3], [3]),
        ([1, 1, 1, 3, 3, 2, 2, 2], [1, 2]),
        ]
for nums, expect in data:
    real = s.majorityElement(nums)
    print(f'{nums} expect {expect} real {real} result {expect == real}')
