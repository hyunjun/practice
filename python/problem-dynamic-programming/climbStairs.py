#   https://leetcode.com/problems/climbing-stairs/

class Solution:
    memo = {0: 0, 1: 1, 2: 2}

    #   95.14%
    def climbStairs(self, n):
        if n in Solution.memo:
            return Solution.memo[n]

        result = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        if n not in Solution.memo:
            Solution.memo[n] = result

        return result

    #   95.14%
    def climbStairsDP(self, n):
        if n <= 0:
            return 0

        result = [0] * n
        result[0] = 1
        if 2 <= n:
            result[1] = 2

        for i in range(2, n):
            result[i] = result[i - 1] + result[i - 2]

        return result[n - 1]


s = Solution()
data = [(2, 2), (3, 3), (10, 89)]
for n, expected in data:
    real = s.climbStairs(n)
    realDP = s.climbStairsDP(n)
    print('inp {}, expected {}, real {}, realDP {} result {}'.format(n, expected, real, realDP, expected == real == realDP))
