#   https://leetcode.com/problems/maximum-score-after-splitting-a-string


class Solution:
    #   runtime; 64ms, 75.00%
    #   memory; 13.6MB, 100.00%
    def maxScore(self, s: str) -> int:
        if s is None or not (2 <= len(s) <= 500):
            return 0
        d = {'0': 0, '1': 0}
        for c in s:
            if c == '1':
                d[c] += 1
        ret = 0
        for i in range(len(s) - 1):
            if '0' == s[i]:
                d['0'] += 1
            else:
                d['1'] -= 1
            ret = max(ret, d['0'] + d['1'])
        return ret


solution = Solution()
data = [('011101', 5),
        ('00111', 5),
        ('1111', 3),
        ('00', 1),
        ]
for s, expected in data:
    real = solution.maxScore(s)
    print(f'{s} expected {expected} real {real} result {expected == real}')
