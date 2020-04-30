#   https://leetcode.com/explore/featured/card/recursion-i/255/recursion-memoization/1662


class Solution:
    #   runtime; 32ms, 32.63%
    #   memory; 13.7MB
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, len(dp)):
            if i == 1:
                dp[i] = 1
            elif i == 2:
                dp[i] = 2
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


s = Solution()
data = [(2, 2),
        (3, 3),
        ]
for n, expected in data:
    real = s.climbStairs(n)
    print(f'{n} expected {expected} real {real} result {expected == real}')
