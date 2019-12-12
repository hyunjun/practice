

class Solution:
    def countWaysRecur(self, num):
        if num == 0:
            return 0

        def count(n):
            if 0 == n:
                return 1
            if n < 3:
                return 0
            cnt = 0
            for c in [3, 5, 10]:
                if c <= n:
                    cnt += count(n - c)
            return cnt

        return count(num)

    def countWaysDP(self, num):
        if num == 0:
            return 0

        dp = [0] * (num + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            for c in [3, 5, 10]:
                if c <= i:
                    dp[i] += dp[i - c]
        return dp[-1]


s = Solution()
data = [(13, 5),
        ]
for num, expected in data:
    real = s.countWaysDP(num)
    print(f'{num} expected {expected} real {real} result {expected == real}')
