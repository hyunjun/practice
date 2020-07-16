#   https://leetcode.com/problems/the-kth-factor-of-n


class Solution:
    #   runtime; 48ms, 42.79%
    #   memory; 13.8MB, 25.00%
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, n + 1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
        return -1


s = Solution()
data = [(12, 3, 3),
        (7, 2, 7),
        (4, 4, -1),
        (1, 1, 1),
        (1000, 3, 4),
        ]
for n, k, expect in data:
    real = s.kthFactor(n, k)
    print(f'{n} {k} expect {expect} real {real} result {expect == real}')
