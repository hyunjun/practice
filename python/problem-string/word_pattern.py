#   https://leetcode.com/problems/word-pattern
#   85.49%


from collections import defaultdict


class Solution:
    def wordPattern0(self, pattern, str):
        if (None == pattern == str) or (0 == len(pattern) == len(str)):
            return True
        if pattern is None or 0 == len(pattern) or str is None or 0 == len(str):
            return False
        strs = str.split(' ')
        if len(pattern) != len(strs):
            return False
        d = {}
        for i, s in enumerate(strs):
            if pattern[i] in d:
                if d[pattern[i]] != s:
                    return False
            else:
                if s in d.values():
                    return False
                d[pattern[i]] = s
        return True

    #   https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3451
    #   runtime; 32ms, 60.84%
    #   memory; 13.9MB, 26.27%
    def wordPattern(self, pattern: str, S: str) -> bool:
        d, strList = defaultdict(set), S.split()
        for p, s in zip(pattern, strList):
            d[p].add(s)
        return len(pattern) == len(strList) and len(set(pattern)) == len(set(strList)) == len(d) and all(len(v) == 1 for v in d.values())


s = Solution()
data = [('abba', 'dog cat cat dog', True),
        ('abba', 'dog cat cat fish', False),
        ('aaaa', 'dog cat cat dog', False),
        ('abba', 'dog dog dog dog', False),
        ('aaa', 'aa aa aa aa', False),
        ('aba', 'dog cat cat', False),
        ]
for pattern, str, expected in data:
    real = s.wordPattern(pattern, str)
    print('{}, {}, expected {}, real {}, result {}'.format(pattern, str, expected, real, expected == real))
