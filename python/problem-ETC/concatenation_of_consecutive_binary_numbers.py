#   https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers


class Solution:
    #   https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3618
    #   runtime; 1244ms, 83.20%
    #   memory; 24.4MB, 14.14%
    def concatenatedBinary(self, n: int) -> int:
        return int(''.join(bin(i)[2:] for i in range(1, n + 1)), 2) % (10 ** 9 + 7)

s = Solution()
data = [(1, 1),
        (3, 27),
        (12, 505379714),
        ]
for n, expect in data:
    real = s.concatenateBinary(n)
    print(f'{n} expect {expect} real {real} result {expect == real}')
