#   https://leetcode.com/problems/count-of-matches-in-tournament


class Solution:
    #   runtime: 36 ms, 24.79%
    #   memory: 14.2 MB, 42.74%
    def numberOfMatches(self, n: int) -> int:
        tot = 0
        while n > 1:
            num = n // 2
            n -= num
            tot += num
        return tot


s = Solution()
data = [(7, 6),
        (14, 13),
        ]
for n, expect in data:
    real = s.numberOfMatches(n)
    print(f'{n} expect {expect} real {real} result {expect == real}')
