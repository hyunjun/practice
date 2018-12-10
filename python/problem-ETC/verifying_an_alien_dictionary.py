#   https://leetcode.com/problems/verifying-an-alien-dictionary

#   https://leetcode.com/problems/verifying-an-alien-dictionary/solution


class Solution:
    #   72ms, 100.00%
    def isAlienSorted(self, words, order):
        d = {}
        for i, c in enumerate(order):
            d[c] = i
        for i, word in enumerate(words):
            if 0 == i:
                continue
            preWord = words[i - 1]
            for j in range(max(len(preWord), len(word))):
                if j < len(word) and d[preWord[j]] < d[word[j]]:
                    break
                if len(word) <= j or d[preWord[j]] > d[word[j]]:
                    return False
        return True


s = Solution()
data = [(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
        (["word","world","row"], "worldabcefghijkmnpqstuvxyz", False),
        (["apple","app"], "abcdefghijklmnopqrstuvwxyz", False),
        ]
for words, order, expected in data:
    real = s.isAlienSorted(words, order)
    print('{}, {}, expected {}, real {}, result {}'.format(words, order, expected, real, expected == real))
