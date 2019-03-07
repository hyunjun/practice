#   https://leetcode.com/problems/top-k-frequent-elements

#   https://leetcode.com/problems/top-k-frequent-elements/solution


from collections import Counter

class Solution:
    #   runtime; 36ms, 80.86%
    #   memory; 12.9MB, 79.67%
    def topKFrequent(self, nums, k):
        if nums is None or 0 == len(nums) or k <= 0:
            return []
        return [n for n, cnt in sorted(Counter(nums).items(), key=lambda t: t[1], reverse=True)][:k]


s = Solution()
data = [([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ]
for nums, k, expected in data:
    real = s.topKFrequent(nums, k)
    print('{}, {}, expected {}, real {}, result {}'.format(nums, k, expected, real, expected == real))
