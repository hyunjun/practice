#   https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
#   100.00%

#   https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/


import sys


class Solution:
    def maxProfit(self, prices):
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
