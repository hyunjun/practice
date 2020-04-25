#   https://leetcode.com/problems/verifying-an-alien-dictionary

#   https://leetcode.com/problems/verifying-an-alien-dictionary/solution


from typing import List


class Solution:
    #   72ms, 100.00%
    def isAlienSorted0(self, words, order):
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

    #   runtime; 40ms, 23.14%
    #   memory; 13.8MB, 5.55%
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if words is None or not (1 <= len(words) <= 100) or 26 != len(order):
            return False
        orderDict = {c: i for i, c in enumerate(order)}
        for r, word in enumerate(words):
            if 0 == r:
                continue
            for c in range(max(len(words[r - 1]), len(word))):
                if c == len(words[r - 1]):
                    break
                if c == len(word):
                    return False
                if words[r - 1][c] == word[c]:
                    continue
                a, b = orderDict[words[r - 1][c]], orderDict[word[c]]
                if a > b:
                    return False
                if a < b:
                    break
        return True


s = Solution()
data = [(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
        (["word","world","row"], "worldabcefghijkmnpqstuvxyz", False),
        (["apple","app"], "abcdefghijklmnopqrstuvwxyz", False),
        ]
for words, order, expected in data:
    real = s.isAlienSorted(words, order)
    print('{}, {}, expected {}, real {}, result {}'.format(words, order, expected, real, expected == real))
