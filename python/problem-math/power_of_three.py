#   https://leetcode.com/problems/power-of-three

#   https://leetcode.com/problems/power-of-three/solution


class Solution:
    #   73.78%
    def isPowerOfThree0(self, n):
        if n <= 0:
            return False
        times = 1
        print('n {} times {}'.format(n, times))
        while times < n and n % times == 0:
            times *= 3
            print('n {} times {}'.format(n, times))
        print('n {} times {}'.format(n, times))
        return n % times == 0

    #   https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3722
    #   runtime; 84ms, 37.40%
    #   memory; 14.3MB, 49.12%
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        while n > 1 and n == int(n):
            n /= 3
        return n == 1


s = Solution()
data = [(0, False),
        (1, True),
        (15, False),
        (-15, False),
        (45, False),
        (228, False),
        ]
for n, expect in data:
    real = s.isPowerOfThree(n)
    print(f'{n}, expect {expect}, real {real}, result {expect == real}')
