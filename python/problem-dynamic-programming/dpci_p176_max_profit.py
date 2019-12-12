

from typing import List


class Solution:
    def maxProfitRecur(self, costs: List[int], length: int) -> int:
        if costs is None or 0 == len(costs):
            return 0

        def getMaxProfit(acc, _costs, _length):
            if _length == 0:
                return acc
            if _length < 0:
                return 0
            subProfit = 0
            for rodLen, cost in _costs:
                if rodLen > _length:
                    continue
                acc += cost
                curProfit = getMaxProfit(acc, _costs, _length - rodLen)
                subProfit = max(subProfit, curProfit)
                acc -= cost
            return subProfit

        return getMaxProfit(0, [(i + 1, cost) for i, cost in enumerate(costs)], length)

    def maxProfit(self, costs: List[int], length: int) -> int:
        if costs is None or 0 == len(costs):
            return 0

        dp = [[0, 0]] * (length + 1)
        dp[0] = [0, 0]
        for d in range(1, length + 1):
            for i, cost in enumerate(costs):
                rodLen = i + 1
                if d < rodLen:
                    continue
                candCost = dp[d - rodLen][1] + cost
                if dp[d][1] < candCost:
                    dp[d] = [dp[d - rodLen][0] + 1, candCost]
        return dp[-1][1]


s = Solution()
data = [([1, 5, 8, 9, 10, 17, 17, 20], 4, 10),
        ]
for costs, length, expected in data:
    real = s.maxProfit(costs, length)
    print(f'{costs} {length} expected {expected} real {real} result {expected == real}')
