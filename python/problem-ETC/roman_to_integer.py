#   https://leetcode.com/problems/roman-to-integer

#   https://leetcode.com/problems/roman-to-integer/discuss/156818/Simple-Python


class Solution:
    #   79.03%
    def romanToInt0(self, s):
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

    #   https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3646/
    #   runtime; 52ms, 46.95%
    #   memory; 14.1MB, 85.09%
    def romanToInt1(self, s: str) -> int:
        twoNumDict = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
        numDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        tot, i = 0, 0
        while i < len(s):
            if i + 1 < len(s):
                if s[i:i + 2] in twoNumDict:
                    tot += twoNumDict[s[i:i + 2]]
                    i += 2
                    continue
            tot += numDict[s[i]]
            i += 1
        return tot

    #   위와 동일. len(s)와 s[i:i + 2] 중복 호출만 제거
    #   runtime; 40ms, 93.59%
    #   memory; 14.4MB
    def romanToInt(self, s: str) -> int:
        twoNumDict = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
        numDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        tot, i, lenS = 0, 0, len(s)
        while i < lenS:
            if i + 1 < lenS:
                twoNums = s[i:i + 2]
                if twoNums in twoNumDict:
                    tot += twoNumDict[twoNums]
                    i += 2
                    continue
            tot += numDict[s[i]]
            i += 1
        return tot


s = Solution()
data = [('III', 3),
        ('IV', 4),
        ('IX', 9),
        ('LVIII', 58),
        ('MCMXCIV', 1994),
        ]
for roman, expect in data:
    real = s.romanToInt(roman)
    print(f'{roman}, expect {expect}, real {real}, result {expect == real}')
