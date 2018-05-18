#   https://leetcode.com/problems/power-of-two
#   72.31%


#   https://leetcode.com/problems/power-of-two/discuss/131043/python-bitwise-solution-beat-97

class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        times = 1
        print('n {} times {}'.format(n, times))
        while times < n and n % times == 0:
            times *= 2
            print('n {} times {}'.format(n, times))
        print('n {} times {}'.format(n, times))
        return n % times == 0


s = Solution()
data = [(0, False), (1, True), (16, True), (-16, False), (218, False)]
for n, expected in data:
    real = s.isPowerOfTwo(n)
    print('{}, expected {}, real {}, result {}'.format(n, expected, real, expected == real))
