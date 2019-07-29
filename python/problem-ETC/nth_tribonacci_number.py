#   https://leetcode.com/problems/n-th-tribonacci-number


class Solution:
    #   runtime; 32ms, 89.63%
    #   memory; 13.8MB, 100.00%
    def tribonacci(self, n: int) -> int:
        if n < 0:
            return 0
        if 0 == n:
            return 0
        if 1 == n or 2 == n:
            return 1
        tn, tn1, tn2 = 0, 1, 1
        for i in range(3, n + 1):
            ans = tn2 + tn1 + tn
            tn, tn1, tn2 = tn1, tn2, ans
        return ans


s = Solution()
data = [(3, 2),
        (4, 4),
        (25, 1389537),
        ]
for n, expected in data:
    real = s.tribonacci(n)
    print(f'{n}, expected {expected}, real {real}, result {expected == real}')
