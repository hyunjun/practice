#   https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero

#   https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/discuss/465174/Python3-One-line-no-condition-check


from typing import List


class Solution:
    #   runtime; 32ms, 60.20%
    #   memory; 12.6MB, 100.00%
    def sumZero(self, n: int) -> List[int]:
        if not (1 <= n <= 1000):
            return []
        res = [i for i in range(1, n)]
        if 1 < n:
            res.append(-1 * n * (n - 1) // 2)
        return res


s = Solution()
data = [(1, [0]),
        (2, [1, -1]),
        (3, [1, 2, -3]),
        (4, [1, 2, 3, -6]),
        ]
for n, expected in data:
    real = s.sumZero(n)
    print(f'{n} expected {expected} real {real} result {expected == real}')
