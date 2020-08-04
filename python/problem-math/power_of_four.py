#   https://leetcode.com/problems/power-of-four

#   https://leetcode.com/problems/power-of-four/discuss/124313/Three-Python-solutions-(Runtime-56-ms-beats-95.94-of-python3-submissions.)


import math


class Solution:
    #   49.33%
    def isPowerOfFour0(self, n):
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

    #   RecursionError
    def isPowerOfFour1(self, num: int) -> bool:
        if not isinstance(num, int) or num % 4 != 0:
            return False
        if num == 4:
            return True
        return self.isPowerOfFour(num // 4)

    #   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3412
    #   runtime; 40ms, 34.75%
    #   memory; 13.9MB
    def isPowerOfFour(self, num: int) -> bool:
        if not isinstance(num, int) or num <= 0 or (1 < num and num % 4 != 0):
            return False
        i = math.log(num, 4)
        return i == (int)(i)


s = Solution()
data = [(0, False),
        (1, True),
        (5, False),
        (8, False),
        (16, True),
        (-16, False),
        (256, True),
        ]
for n, expect in data:
    real = s.isPowerOfFour(n)
    print(f'{n}, expect {expect}, real {real}, result {expect == real}')
