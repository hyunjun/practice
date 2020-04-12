#   https://leetcode.com/problems/string-matching-in-an-array

#   https://leetcode.com/problems/string-matching-in-an-array/discuss/575147/Clean-Python-3-suffix-trie-O(NlogN-%2B-N-*-S2)


from typing import List


class Solution:
    #   runtime; 32ms, 100.00%
    #   memory; 13.7MB, 100.00%
    def stringMatching(self, words: List[str]) -> List[str]:
        if words is None or not (1 <= len(words) <= 100):
            return []
        res, sortedWords = [], sorted(words, key=lambda t: len(t))
        for i, word in enumerate(sortedWords):
            for j in range(i + 1, len(sortedWords)):
                if word in sortedWords[j]:
                    res.append(word)
                    break
        return res


s = Solution()
data = [(["mass","as","hero","superhero"], ["as","hero"]),
        (["leetcode","et","code"], ["et","code"]),
        (["blue","green","bu"], []),
        ]
for words, expected in data:
    real = s.stringMatching(words)
    print(f'{words} expected {expected} real {real} result {expected == real}')
