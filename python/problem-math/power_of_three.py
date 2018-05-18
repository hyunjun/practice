#   https://leetcode.com/problems/power-of-three
#   73.78%

#   https://leetcode.com/problems/power-of-three/solution


class Solution:
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        times = 1
        print('n {} times {}'.format(n, times))
        while times < n and n % times == 0:
            times *= 3
            print('n {} times {}'.format(n, times))
        print('n {} times {}'.format(n, times))
        return n % times == 0

s = Solution()
data = [(0, False), (1, True), (15, False), (-15, False), (45, False), (228, False)]
for n, expected in data:
    real = s.isPowerOfThree(n)
    print('{}, expected {}, real {}, result {}'.format(n, expected, real, expected == real))
