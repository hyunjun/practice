#   https://leetcode.com/problems/largest-substring-between-two-equal-characters


class Solution:
    #   runtime; 16ms, 100.00%
    #   memory; 14.2MB, 100.00%
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        for i, c in enumerate(s):
            if c not in d:
                d[c] = [float('inf'), float('-inf')]
            d[c][0] = min(d[c][0], i)
            d[c][1] = max(d[c][0], i)
        return max(maxIdx - minIdx - 1 for minIdx, maxIdx in d.values())


solution = Solution()
data = [('aa', 0),
        ('abca', 2),
        ('cbzxy', -1),
        ('cabbac', 4),
        ]
for s, expect in data:
    real = solution.maxLengthBetweenEqualCharacters(s)
    print(f'{s} expect {expect} real {real} result {expect == real}')
