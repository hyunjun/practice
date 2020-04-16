#   https://leetcode.com/problems/sort-integers-by-the-power-value


class Solution:
    #   runtime; 240ms, 63.38%
    #   memory; 28.7MB, 100.00%
    def getKth(self, lo: int, hi: int, k: int) -> int:
        if not (1 <= lo <= 1000) or not (1 <= hi <= 1000) or not (1 <= k <= hi - lo + 1):
            return 0

        d = {}
        def power(nums, n, acc):
            nums.append(n)
            if n in d:
                acc += d[n]
                for num in nums:
                    d[num] = acc
                    acc -= 1
            elif n == 1:
                for num in nums:
                    d[num] = acc
                    acc -= 1
            else:
                if n % 2 == 0:
                    power(nums, n // 2, acc + 1)
                else:
                    power(nums, 3 * n + 1, acc + 1)

        for i in range(lo, hi + 1):
            if i not in d:
                power([], i, 0)

        return sorted([i for i in range(lo, hi + 1)], key=lambda i: d[i])[k - 1]


s = Solution()
data = [(12, 15, 2, 13),
        (1, 1, 1, 1),
        (7, 11, 4, 7),
        (10, 20, 5, 13),
        (1, 1000, 777, 570),
        ]
for lo, hi, k, expected in data:
    real = s.getKth(lo, hi, k)
    print(f'{lo} {hi} {k} expected {expected} real {real} result {expected == real}')
