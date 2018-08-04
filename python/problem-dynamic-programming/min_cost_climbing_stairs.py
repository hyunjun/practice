#   https://leetcode.com/problems/min-cost-climbing-stairs

#   https://leetcode.com/problems/min-cost-climbing-stairs/solution


class Solution:
    #   50.18%
    def minCostClimbingStairs(self, cost):
        if 2 == len(cost):
            return min(cost)
        dp = [0] * len(cost)
        for i in range(2, len(cost)):
            dp[i] = min(cost[i - 2] + dp[i - 2], cost[i - 1] + dp[i - 1])
        return min(cost[-2] + dp[-2], cost[-1] + dp[-1])


s = Solution()
data = [([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
        ]
for cost, expected in data:
    real = s.minCostClimbingStairs(cost)
    print('{}, expected {}, real {}, result {}'.format(cost, expected, real, expected == real))
