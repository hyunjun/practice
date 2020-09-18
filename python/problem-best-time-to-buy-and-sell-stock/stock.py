# https://leetcode.com/problems/best-time-to-buy-and-sell-stock


from typing import List


class Solution:
    def maxProfit0(self, prices):
        if prices is None or 0 == len(prices):
            return 0

        cur_min = cur_max = prices[0]
        result = 0
        for p in prices[1:]:
            if p < cur_min:
                cur_min = cur_max = p
            if cur_max < p:
                cur_max = p
            if result < cur_max - cur_min:
                result = cur_max - cur_min
        return result

    #   https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3464
    #   runtime; 64ms, 76.46%
    #   memory; 15MB, 83.96%
    def maxProfit1(self, prices: List[int]) -> int:
        if prices is None or 0 == len(prices):
            return 0
        minPrice, maxProfit = prices[0], 0
        for i, p in enumerate(prices):
            if 0 == i:
                continue
            if p < minPrice:
                minPrice = p
            else:
                maxProfit = max(maxProfit, p - minPrice)
        return maxProfit

    #   runtime; 72ms, 45.05%
    #   memory; 15.2MB, 32.64%
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or 0 == len(prices):
            return 0
        minPrice, maxProfit = prices[0], 0
        for i, p in enumerate(prices):
            minPrice = min(minPrice, p)
            maxProfit = max(maxProfit, p - minPrice)
        return maxProfit


s = Solution()
cases = [([7, 1, 5, 3, 6, 4], 5),
         ([7, 6, 4, 3, 1], 0),
         ([2, 4, 1], 2),
         ]
for prices, expect in cases:
    real = s.maxProfit(prices)
    print(f'{prices} expect {expect} real {real} result {expect == real}')
