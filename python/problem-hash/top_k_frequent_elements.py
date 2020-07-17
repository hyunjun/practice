#   https://leetcode.com/problems/top-k-frequent-elements

#   https://leetcode.com/problems/top-k-frequent-elements/solution


from collections import Counter
from typing import List


class Solution:
    #   runtime; 36ms, 80.86%
    #   memory; 12.9MB, 79.67%
    def topKFrequent(self, nums, k):
        if nums is None or 0 == len(nums) or k <= 0:
            return []
        return [n for n, cnt in sorted(Counter(nums).items(), key=lambda t: t[1], reverse=True)][:k]

    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3393
    #   runtime; 168ms, 18.92%
    #   memory; 18.3MB, 59.71%
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [n for n, _ in sorted(Counter(nums).items(), key=lambda t: -t[1])[:k]]


s = Solution()
data = [([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ]
for nums, k, expected in data:
    real = s.topKFrequent(nums, k)
    print('{}, {}, expected {}, real {}, result {}'.format(nums, k, expected, real, expected == real))
