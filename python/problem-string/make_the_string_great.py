#   https://leetcode.com/problems/make-the-string-great


class Solution:
    #   runtime; 36ms, 77.79%
    #   memory; 13.8MB, 65.86%
    def makeGood(self, s: str) -> str:
        if len(s) <= 1 or s.islower():
            return s
        for i, c in enumerate(s):
            if i + 1 < len(s) and c.lower() == s[i + 1].lower() and ((c.islower() and s[i + 1].isupper()) or (c.isupper() and s[i + 1].islower())):
                return self.makeGood(s[:i] + s[i + 2:])
        return s


solution = Solution()
data = [('leEeetcode', 'leetcode'),
        ('abBAcC', ''),
        ('mC', 'mC'),
        ('Hvh', 'Hvh'),
        ]
for s, expect in data:
    real = solution.makeGood(s)
    print(f'{s} expect {expect} real {real} result {expect == real}')
