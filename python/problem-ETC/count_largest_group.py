#   https://leetcode.com/problems/count-largest-group


from collections import defaultdict


class Solution:
    #   runtime; 140ms, 31.87%
    #   memory; 14.1MB, 100.00%
    def countLargestGroup(self, n: int) -> int:
        if not (1 <= n <= 10 ** 4):
            return 0
        d = defaultdict(list)
        for i in range(1, n + 1):
            k = sum(int(s) for s in str(i))
            d[k].append(i)
        maxSize = max(len(v) for v in d.values())
        return sum(1 if len(v) == maxSize else 0 for v in d.values())


s = Solution()
data = [(13, 4),
        (2, 2),
        (15, 6),
        (24, 5),
        ]
for n, expected in data:
    real = s.countLargestGroup(n)
    print(f'{n} expected {expected} real {real} result {expected == real}')
