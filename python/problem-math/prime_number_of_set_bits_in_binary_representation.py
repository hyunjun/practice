#   https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation

#   https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/solution


class Solution:
    #   4.35%
    def countPrimeSetBits(self, L, R):
        def numberOfBits(n):
            cnt = 0
            while 0 < n:
                if n & 0x1:
                    cnt += 1
                n >>= 1
            return cnt
        def isPrime(n):
            if n in [2, 3, 5, 7, 11, 13, 17, 19]:
                return True
            return False
        cnt = 0
        for i in range(L, R + 1):
            num = numberOfBits(i)
            if isPrime(num):
                cnt += 1
        return cnt


s = Solution()
data = [(6, 10, 4),
        (10, 15, 5),
        ]
for L, R, expected in data:
    real = s.countPrimeSetBits(L, R)
    print('{}, {}, expected {}, real {}, result {}'.format(L, R, expected, real, expected == real))
