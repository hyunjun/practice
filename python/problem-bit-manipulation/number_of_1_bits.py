#   https://leetcode.com/problems/number-of-1-bits

#   https://leetcode.com/problems/number-of-1-bits/solution


class Solution:
    #   74.76%
    def hammingWeight0(self, n):
        cnt, bit = 0, 0x1
        while bit <= n:
            if 0 != n & bit:
                cnt += 1
            bit <<= 1
        return cnt

    #   https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3625
    #   runtime; 44ms, 10.16%
    #   memory; 14.1MB, 70.08%
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


s = Solution()
data = [(11, 3),
        (128, 1),
        ]
for n, expect in data:
    real = s.hammingWeight(n)
    print(f'{n}, expect {expect}, real {real}, result {expect == real}')
