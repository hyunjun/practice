#   https://leetcode.com/problems/detect-capital


class Solution:
    #   74.48%
    def detectCapitalUse(self, word):
        if word is None or 0 == len(word):
            return False
        if all(['A' <= w <= 'Z' for w in word]) or all(['a' <= w <= 'z' for w in word]):
            return True
        for i in range(1, len(word)):
            if 'A' <= word[i] <= 'Z':
                return False
        return True


s = Solution()
data = [('USA', True),
        ('FlaG', False),
        ('leetcode', True),
        ('Google', True),
        ]
for word, expected in data:
    real = s.detectCapitalUse(word)
    print('{}, expected {}, real {}, result {}'.format(word, expected, real, expected == real))
