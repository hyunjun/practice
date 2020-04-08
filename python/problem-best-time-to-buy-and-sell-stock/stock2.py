#   https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

#   https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/


import sys


class Solution:
    #   100.00%
    def maxProfit0(self, prices):
        if prices is None or 0 == len(prices):
            return 0
        b, s = sys.maxsize, sys.maxsize
        profits, curProfit = [], 0
        for p in prices:
            if s < p:
                s = p
                curProfit = s - b
            else:
                #print('{} ~ {}, {}'.format(b, s, curProfit))
                b = s = p
                if 0 < curProfit:
                    profits.append(curProfit)
                    curProfit = 0
        #print('{} ~ {}, {}'.format(b, s, curProfit))
        if 0 < curProfit:
            profits.append(curProfit)
        return sum(profits)

    #   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3287
    #   runtime; 68ms, 40.43%
    #   memory; 15.2MB
    def maxProfit(self, prices):
        if prices is None or not (1 <= len(prices) <= 3 * 10 ** 4):
            return 0
        curMin, curMax, profit = prices[0], None, 0
        for i in range(1, len(prices)):
            if prices[i - 1] >= prices[i]:
                if curMax is not None:
                    profit += curMax - curMin
                    curMax = None
                curMin = prices[i]
            elif prices[i - 1] < prices[i]:
                curMax = prices[i]
        if curMax is not None:
            profit += curMax - curMin
        return profit


s = Solution()
data = [([7, 1, 5, 3, 6, 4], 7),
        ([7, 1, 5, 3, 6], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
        ([1, 7, 2, 3, 6, 7, 6, 7], 12)
        ]
for prices, expected in data:
    real = s.maxProfit(prices)
    print('{}, expected {}, real {}, result {}'.format(prices, expected, real, expected == real))
