#   https://leetcode.com/problems/student-attendance-record-i


class Solution:

    #   Wrong Answer, misunderstand
    def checkRecord0(self, s):
        if s is None or 0 == len(s):
            return True
        d = {'A': 0, 'L': 0, 'P': 0}
        for c in s:
            d[c] += 1
        return d['A'] <= 1 and d['L'] <= 2

    #   Wrong Answer
    def checkRecord1(self, s):
        if s is None or 0 == len(s):
            return True
        d = {'A': 0, 'L': 0, 'P': 0}
        d[s[0]] += 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                d[s[i]] += 1
                if 'A' == s[i]:
                    if 1 < d['A']:
                        return False
                elif 'L' == s[i]:
                    if 2 < d['L']:
                        return False
            else:
                d[s[i]] = 1
        return True

    #   문제 설명이 안 좋음
    def checkRecord(self, s):
        return s.count('A') <= 1 and 0 == s.count('LLL')


solution = Solution()
data = [('', True),
        ('PPALLP', True),
        ('PPALLL', False),
        ('LALL', True),
        ('ALLAPPL', False),
        ]
for s, expected in data:
    real = solution.checkRecord(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
