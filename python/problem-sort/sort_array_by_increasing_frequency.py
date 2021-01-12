#   https://leetcode.com/problems/sort-array-by-increasing-frequency


from collections import Counter
from typing import List


class Solution:
    #   runtime; 52ms, 57.28%
    #   memory; 14.4MB, 20.71%
    def frequencySort(self, nums: List[int]) -> List[int]:
        ret = []
        for n, cnt in sorted(Counter(nums).items(), key=lambda t: (t[1], -t[0])):
            ret.extend([n] * cnt)
        return ret


s = Solution()
data = [([1,1,2,2,2,3], [3,1,1,2,2,2]),
        ([2,3,1,3,2], [1,3,3,2,2]),
        ([-1,1,-6,4,5,-6,1,4,1], [5,-1,4,4,-6,-6,1,1,1]),
        ]
for nums, expect in data:
    real = s.frequencySort(nums)
    print(f'{nums} expect {expect} real {real} result {expect == real}')
