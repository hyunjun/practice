#   https://leetcode.com/problems/greatest-common-divisor-of-strings


class Solution:
    #   Wrong Answer
    def gcdOfStrings0(self, str1: str, str2: str) -> str:
        if str1 is None or str2 is None or 0 == len(str1) or 0 == len(str2):
            return ''

        if len(str1) < len(str2):
            longer, shorter = str2, str1
        elif len(str1) > len(str2):
            longer, shorter = str1, str2
        else:
            if str1 == str2:
                return str1
            return ''

        def getPattern(s):
            i, pattern = 0, None
            while i < len(s) // 2:
                front, rear = s[0:i + 1], s[-(i + 1):]
                if front == rear:
                    pattern = front
                i += 1
            if pattern is None:
                return s
            return pattern

        lPattern, sPattern = getPattern(longer), getPattern(shorter)
        if lPattern == sPattern:
            return lPattern
        if sPattern in lPattern:
            return sPattern
        return ''

    #   Wrong Answer
    def gcdOfStrings1(self, str1: str, str2: str) -> str:
        if str1 is None or str2 is None or 0 == len(str1) or 0 == len(str2):
            return ''

        if len(str1) < len(str2):
            longer, shorter = str2, str1
        elif len(str1) > len(str2):
            longer, shorter = str1, str2
        else:
            if str1 == str2:
                return str1
            return ''

        def getPatterns(s):
            i, patterns = 0, [s]
            while i < len(s) // 2:
                front, rear = s[0:i + 1], s[-(i + 1):]
                if front == rear:
                    patterns.append(front)
                i += 1
            return patterns

        lPatterns, sPatterns = getPatterns(longer), getPatterns(shorter)
        for l in lPatterns:
            for s in sPatterns:
                if l == s:
                    return l
        return ''

    #   runtime; 44ms, 29.20%
    #   memory; 13.1MB, 100.00%
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 is None or str2 is None or 0 == len(str1) or 0 == len(str2):
            return ''

        if len(str1) < len(str2):
            longer, shorter = str2, str1
        elif len(str1) > len(str2):
            longer, shorter = str1, str2
        else:
            if str1 == str2:
                return str1
            return ''

        def getPatterns(s):
            i, patterns = 0, []
            while i < len(s) // 2:
                front, rear = s[0:i + 1], s[-(i + 1):]
                if front == rear:
                    length = len(s) // len(front)
                    if s == length * front:
                        patterns.append(front)
                i += 1
            patterns.append(s)
            return patterns[::-1]

        lPatterns, sPatterns = getPatterns(longer), getPatterns(shorter)
        for l in lPatterns:
            for s in sPatterns:
                if l == s:
                    return l
        return ''


s = Solution()
data = [('ABCABC', 'ABC', 'ABC'),
        ('ABABAB', 'ABAB', 'AB'),
        ('LEET', 'CODE', ''),
        ('TAUXXTAUXXTAUXXTAUXXTAUXX', 'TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX', 'TAUXX'),
        ('OBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNO', 'OBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNO', 'OBCNO'),
        ]
for str1, str2, expected in data:
    real = s.gcdOfStrings(str1, str2)
    print(f'{str1}, {str2}, expected {expected}, real {real}, result {expected == real}')
