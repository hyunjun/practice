#   https://leetcode.com/problems/coin-change-2

#   https://leetcode.com/problems/coin-change-2/discuss/674977/100-Faster-or-Recursive-1-d-2-d-DP-or-Matrix-With-Example-or-Commented-Code-Video


from typing import List


class Solution:
    #   https://leetcode.com/explore/featured/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3353
    #   runtime; 140ms, 81.09%
    #   memory; 14.1MB
    def change(self, amount: int, coins: List[int]) -> int:
        if amount <= 0:
            return 1
        if coins is None or not (1 <= len(coins) <= 5000):
            return 0
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, len(dp)):
                dp[i] += dp[i - c]
        return dp[-1]


s = Solution()
data = [(5, [1, 2, 5], 4),
        (3, [2], 0),
        (10, [10], 1),
        (0, [], 1),
        (7, [], 0),
        ]
for amount, coins, expect in data:
    real = s.change(amount, coins)
    print(f'{amount} {coins} expect {expect} real {real} result {expect == real}')
