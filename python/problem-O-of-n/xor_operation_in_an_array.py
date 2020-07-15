#   https://leetcode.com/problems/xor-operation-in-an-array


from functools import reduce


class Solution:
    #   runtime; 32ms, 65.30%
    #   memory; 14MB, 100.00%
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(lambda a, b: a ^ b, [start + 2 * i for i in range(n)])


s = Solution()
data = [(5, 0, 8),
        (4, 3, 8),
        (1, 7, 7),
        (10, 5, 2),
        ]
for n, start, expect in data:
    real = s.xorOperation(n, start)
    print(f'{n} {start} expect {expect} real {real} result {expect == real}')
