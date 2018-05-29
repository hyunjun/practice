#   https://leetcode.com/problems/word-pattern
#   85.49%


class Solution:
    def wordPattern(self, pattern, str):
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


s = Solution()
data = [('abba', 'dog cat cat dog', True),
        ('abba', 'dog cat cat fish', False),
        ('aaaa', 'dog cat cat dog', False),
        ('abba', 'dog dog dog dog', False),
        ('aaa', 'aa aa aa aa', False),
        ]
for pattern, str, expected in data:
    real = s.wordPattern(pattern, str)
    print('{}, {}, expected {}, real {}, result {}'.format(pattern, str, expected, real, expected == real))
