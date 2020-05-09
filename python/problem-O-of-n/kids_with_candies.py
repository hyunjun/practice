#   https://leetcode.com/problems/kids-with-the-greatest-number-of-candies


from typing import List


class Solution:
    #   runtime; 36ms, 78.44%
    #   memory; 13.8MB, 100.00%
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        if candies is None or not (2 <= len(candies) <= 100) or not (1 <= extraCandies <= 50):
            return []
        maxCandy = max(candies)
        return [True if candy + extraCandies >= maxCandy else False for candy in candies]


s = Solution()
data = [([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
        ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
        ([12, 1, 12], 10, [True, False, True]),
        ]
for candies, extraCandies, expected in data:
    real = s.kidsWithCandies(candies, extraCandies)
    print(f'{candies} {extraCandies} expected {expected} real {real} result {expected == real}')
