#   https://leetcode.com/problems/most-visited-sector-in-a-circular-track


from collections import defaultdict
from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        d = defaultdict(int)
        d[rounds[0]] += 1
        for i in range(1, len(rounds)):
            s, e = rounds[i - 1], rounds[i]
            if s < e:
                for j in range(s + 1, e + 1):
                    d[j] += 1
            else:
                for j in range(s + 1, n + 1):
                    d[j] += 1
                for j in range(1, e + 1):
                    d[j] += 1
        return sorted(r for r, c in d.items() if c == max(d.values()))


s = Solution()
data = [(4, [1, 3, 1, 2], [1, 2]),
        (2, [2, 1, 2, 1, 2, 1, 2, 1, 2], [2]),
        (7, [1, 3, 5, 7], [1, 2, 3, 4, 5, 6, 7]),
        ]
for n, rounds, expect in data:
    real = s.mostVisited(n, rounds)
    print(f'{n} {rounds} expect {expect} real {real} result {expect == real}')
