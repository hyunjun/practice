

from typing import List


class Solution:
    def minCoins(self, coins: List[int], money: int) -> int:
        if coins is None or 0 == len(coins):
            return 0

        dp = [float('inf')] * (money + 1)
        dp[0] = 0
        for m in range(1, money + 1):
            for coin in coins:
                if m < coin:
                    continue
                elif m == coin:
                    dp[m] = 1
                else:
                    if dp[m - coin] > 0:
                        dp[m] = min(dp[m], 1 + dp[m - coin])
        return dp[-1]


s = Solution()
data = [([1, 5, 6, 9], 11, 2),
        ([1, 2, 5, 10, 20, 50], 65, 3),
        ([1, 2, 5, 10, 15, 50], 65, 2),
        ]
for coins, money, expected in data:
    real = s.minCoins(coins, money)
    print(f'{coins} {money} expected {expected} real {real} result {expected == real}')
