#   https://leetcode.com/problems/roman-to-integer

#   https://leetcode.com/problems/roman-to-integer/discuss/156818/Simple-Python


class Solution:
    #   79.03%
    def romanToInt(self, s):
        i, cnt = 0, 0
        while i < len(s):
            if 'I' == s[i]:
                if i + 1 < len(s) and s[i + 1] in ['V', 'X']:
                    if 'V' == s[i + 1]:
                        cnt += 4
                    elif 'X' == s[i + 1]:
                        cnt += 9
                    i += 2
                else:
                    cnt += 1
                    i += 1
            elif 'V' == s[i]:
                cnt += 5
                i += 1
            elif 'X' == s[i]:
                if i + 1 < len(s) and s[i + 1] in ['L', 'C']:
                    if 'L' == s[i + 1]:
                        cnt += 40
                    elif 'C' == s[i + 1]:
                        cnt += 90
                    i += 2
                else:
                    cnt += 10
                    i += 1
            elif 'L' == s[i]:
                cnt += 50
                i += 1
            elif 'C' == s[i]:
                if i + 1 < len(s) and s[i + 1] in ['D', 'M']:
                    if 'D' == s[i + 1]:
                        cnt += 400
                    elif 'M' == s[i + 1]:
                        cnt += 900
                    i += 2
                else:
                    cnt += 100
                    i += 1
            elif 'D' == s[i]:
                cnt += 500
                i += 1
            elif 'M' == s[i]:
                cnt += 1000
                i += 1
        return cnt


s = Solution()
data = [('III', 3),
        ('IV', 4),
        ('IX', 9),
        ('LVIII', 58),
        ('MCMXCIV', 1994),
        ]
for roman, expected in data:
    real = s.romanToInt(roman)
    print('{}, expected {}, real {}, result {}'.format(roman, expected, real, expected == real))
