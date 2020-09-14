#   https://leetcode.com/problems/number-of-good-ways-to-split-a-string


from collections import Counter
from collections import defaultdict


class Solution:
    #   runtime; 1304ms, 5.80%
    #   memory; 14.3MB, 99.37%
    def numSplits(self, s: str) -> int:
        cnt, lc, rc = 0, defaultdict(int), Counter(s)
        for c in s:
            lc[c] += 1
            rc[c] -= 1
            if len([ch for ch, v in lc.items() if v > 0]) == len([ch for ch, v in rc.items() if v > 0]):
                cnt += 1
        return cnt


solution = Solution()
data = [("aacaba", 2),
        ("abcd", 1),
        ("aaaaa", 4),
        ("acbadbaada", 2),
        ]
for s, expect in data:
    real = solution.numSplits(s)
    print(f'{s} expect {expect} real {real} result {expect == real}')
