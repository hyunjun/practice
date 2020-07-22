#   https://leetcode.com/problems/water-bottles


class Solution:
    #   runtime; 32ms, 84.13%
    #   memory; 13.9MB, 100.00%
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while numBottles >= numExchange:
            newBottles = numBottles // numExchange
            numBottles = newBottles + numBottles % numExchange
            total += newBottles
        return total


s = Solution()
data = [(9, 3, 13),
        (15, 4, 19),
        ]
for numBottles, numExchange, expect in data:
    real = s.numWaterBottles(numBottles, numExchange)
    print(f'{numBottles} {numExchange} expect {expect} real {real} result {expect == real}')
