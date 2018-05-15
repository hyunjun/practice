#   https://leetcode.com/problems/number-of-1-bits
#   74.76%

#   https://leetcode.com/problems/number-of-1-bits/solution


class Solution:
    def hammingWeight(self, n):
        cnt, bit = 0, 0x1
        while bit <= n:
            if 0 != n & bit:
                cnt += 1
            bit <<= 1
        return cnt


s = Solution()
data = [(11, 3), (128, 1)]
for n, expected in data:
    real = s.hammingWeight(n)
    print('{}, expected {}, real {}, result {}'.format(n, expected, real, expected == real))
