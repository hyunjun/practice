#   https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop


from typing import List


class Solution:
    #   Wrong Answer
    def finalPrices0(self, prices: List[int]) -> List[int]:
        mins = prices[:]
        for i in range(len(mins) - 2, -1, -1):
            mins[i] = min(mins[i], mins[i + 1])
        for i in range(len(prices) - 1):
            if prices[i + 1] <= prices[i]:
                prices[i] -= prices[i + 1]
            elif mins[i + 1] <= prices[i]:
                prices[i] -= mins[i + 1]
        return prices

    #   runtime; 52ms, 87.45%
    #   memory; 14MB, 50.00%
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i, p in enumerate(prices):
            for j in range(i + 1, len(prices)):
                if prices[j] <= p:
                    prices[i] -= prices[j]
                    break
        return prices


s = Solution()
data = [([8,4,6,2,3], [4,2,4,2,3]),
        ([1,2,3,4,5], [1,2,3,4,5]),
        ([10,1,1,6], [9,0,1,6]),
        ([5,4,10,2,6,1,1,1,9,1], [1,2,8,1,5,0,0,0,8,1]),
        ]
for prices, expect in data:
    real = s.finalPrices(prices)
    print(f'{prices} expect {expect} real {real} result {expect == real}')
