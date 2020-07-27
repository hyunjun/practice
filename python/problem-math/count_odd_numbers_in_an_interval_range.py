#   https://leetcode.com/problems/count-odd-numbers-in-an-interval-range


class Solution:
    #   runtime; 28ms, 88.63%
    #   memory; 14MB, 100.00%
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1
        if high % 2 == 0:
            high -= 1
        return (high - low) // 2 + 1


s = Solution()
data = [(3, 7, 3),
        (8, 10, 1),
        (800445804, 979430543, 89492370),
        ]
for low, high, expect in data:
    real = s.countOdds(low, high)
    print(f'{low} {high} expect {expect} real {real} result {expect == real}')
