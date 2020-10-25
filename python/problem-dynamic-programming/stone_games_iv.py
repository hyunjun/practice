#   https://leetcode.com/problems/stone-game-iv

#   https://leetcode.com/problems/stone-game-iv/solution


from collections import defaultdict
import math


class Solution:
    #   https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3507
    #   runtime; 3736ms, 26.49%
    #   memory; 14.8MB
    def winnerSquareGame(self, n: int) -> bool:

        dp = [False] * (n + 1)
        stones = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]
        for i in range(1, len(dp)):
            for stone in stones:
                if i < stone:
                    continue
                if not dp[i - stone]:
                    dp[i] = True
        return dp[-1]


s = Solution()
data = [(1, True),
        (2, False),
        (4, True),
        (7, False),
        (17, False),
        ]
for n, expect in data:
    real = s.winnerSquareGame(n)
    print(f'{n} expect {expect} real {real} result {expect == real}')
