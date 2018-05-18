#   https://leetcode.com/problems/power-of-four
#   49.33%

#   https://leetcode.com/problems/power-of-four/discuss/124313/Three-Python-solutions-(Runtime-56-ms-beats-95.94-of-python3-submissions.)

import math


class Solution:
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        i = math.log(n, 4)
        return i == (int)(i)
        #return 0 < n and 1073741824 % n == 0
        '''
        if n <= 0:
            return False
        times = 1
        print('n {} times {}'.format(n, times))
        while times < n and n % times == 0:
            times *= 4
            print('n {} times {}'.format(n, times))
        print('n {} times {}'.format(n, times))
        return n % times == 0
        '''


s = Solution()
data = [(0, False), (1, True), (5, False), (8, False), (16, True), (-16, False), (256, True)]
for n, expected in data:
    real = s.isPowerOfFour(n)
    print('{}, expected {}, real {}, result {}'.format(n, expected, real, expected == real))
