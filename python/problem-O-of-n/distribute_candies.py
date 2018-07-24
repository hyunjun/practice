#   https://leetcode.com/problems/distribute-candies

#   https://leetcode.com/problems/distribute-candies/solution


from collections import Counter


class Solution:
    #   30.66%
    def distributeCandies(self, candies):
        if candies is None or 0 == len(candies):
            return 0
        counter = Counter(candies)
        halfLen = len(candies) // 2
        keyLen = len(counter.keys())
        if halfLen <= keyLen:
            return halfLen
        return keyLen


s = Solution()
data = [([1, 1, 1, 1, 1, 1], 1),
        ([1, 1, 1, 1, 1, 2], 2),
        ([1, 1, 1, 1, 2, 3], 3),
        ([1, 1, 1, 2, 3, 4], 3),
        ([1, 1, 2, 2, 3, 3], 3),
        ([1, 1, 2, 3], 2),
        ]
for candies, expected in data:
    real = s.distributeCandies(candies)
    print('{}, expected {}, real {}, result {}'.format(candies, expected, real, expected == real))
