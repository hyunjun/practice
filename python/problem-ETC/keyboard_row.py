#   https://leetcode.com/problems/keyboard-row

#   https://leetcode.com/problems/keyboard-row/discuss/151186/Python3-Beat-100-by-Simida


class Solution:
    #   100.00%
    def findWords(self, words):
        d = {'q': 0, 'w': 0, 'e': 0, 'r': 0, 't': 0, 'y': 0, 'u': 0, 'i': 0, 'o': 0, 'p': 0,
             'a': 1, 's': 1, 'd': 1, 'f': 1, 'g': 1, 'h': 1, 'j': 1, 'k': 1, 'l': 1,
             'z': 2, 'x': 2, 'c': 2, 'v': 2, 'b': 2, 'n': 2, 'm': 2}
        res = []
        for word in words:
            s = set()
            for c in word.lower():
                s.add(d[c])
            if 1 == len(s):
                res.append(word)
        return res


s = Solution()
data = [(['Hello', 'Alaska', 'Dad', 'Peace'], ['Alaska', 'Dad']),
        ]
for words, expected in data:
    real = s.findWords(words)
    print('{}, expected {}, real {}, result {}'.format(words, expected, real, expected == real))
