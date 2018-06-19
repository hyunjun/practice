#   https://leetcode.com/problems/count-primes

#   https://leetcode.com/problems/count-primes/discuss/134754/Python-Solution-beats-99.80

class Solution:
    d = {2: True, 3: True}

    def isPrime(self, n):
        if n in Solution.d:
            return Solution.d[n]
        for p in Solution.d.keys():
            if 0 == n % p:
                Solution.d[n] = False
                return False
        for i in range(n // 2, 1, -1):
            if n % i == 0:
                Solution.d[n] = False
                return False
        Solution.d[n] = True
        return True

    #   Time Limit Exceeded
    def countPrimes0(self, n):
        cnt = 0
        for i in range(2, n):
            if self.isPrime(i):
                cnt += 1
        return cnt

    #   13.61%
    def countPrimes(self, n):
        if n < 2:
            return 0
        cnt = 0
        nums = list(range(n))
        nums[0], nums[1] = None, None
        for num in nums:
            if num is None:
                continue
            m = 2
            while m * num < n:
                nums[m * num] = None
                m += 1
        cnt = 0
        for num in nums:
            if num:
                cnt += 1
        return cnt


s = Solution()
data = [(10, 4), (2, 0), (499979, 41537)]
for n, expected in data:
    real = s.countPrimes(n)
    print('{}, expected {}, real {}, result {}'.format(n, expected, real, expected == real))
