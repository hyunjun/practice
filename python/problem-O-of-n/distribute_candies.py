#   https://leetcode.com/problems/distribute-candies

#   https://leetcode.com/problems/distribute-candies/solution


from collections import Counter
from typing import List


class Solution:
    #   30.66%
    def distributeCandies0(self, candies):
        if candies is None or 0 == len(candies):
            return 0
        counter = Counter(candies)
        halfLen = len(candies) // 2
        keyLen = len(counter.keys())
        if halfLen <= keyLen:
            return halfLen
        return keyLen

    #   https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3657
    #   runtime: 908ms, 17.91%
    #   memory: 16.8MB
    def distributeCandies1(self, candyType: List[int]) -> int:
        n, c = len(candyType) // 2, sorted(Counter(candyType).items(), key=lambda t: t[1])
        if len(c) < n:
            return len(c)
        return n

    #   runtime: 844ms, 32.32%
    #   memory: 16MB, 94.46%
    def distributeCandies2(self, candyType: List[int]) -> int:
        n, cLen = len(candyType) // 2, len(Counter(candyType).keys())
        if cLen < n:
            return cLen
        return n

    #   runtime: 820ms, 42.94%
    #   memory: 16.3MB, 66.24%
    def distributeCandies(self, candyType: List[int]) -> int:
        n, cLen = len(candyType) // 2, len(set(candyType))
        if cLen < n:
            return cLen
        return n


s = Solution()
data = [([1, 1, 1, 1, 1, 1], 1),
        ([1, 1, 1, 1, 1, 2], 2),
        ([1, 1, 1, 1, 2, 3], 3),
        ([1, 1, 1, 2, 3, 4], 3),
        ([1, 1, 2, 2, 3, 3], 3),
        ([1, 1, 2, 3], 2),
        ]
for candies, expect in data:
    real = s.distributeCandies(candies)
    print(f'{candies}, expect {expect}, real {real}, result {expect == real}')
