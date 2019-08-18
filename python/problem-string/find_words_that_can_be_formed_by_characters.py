#   https://leetcode.com/problems/find-words-that-can-be-formed-by-characters   

#   https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/discuss/360959/Python-One-line-solution


from collections import Counter
from typing import List


class Solution:
    #   runtime; 216ms, 100.00%
    #   memory; 14.2MB, 100.00%
    def countCharacters(self, words: List[str], chars: str) -> int:
        if words is None or 0 == len(words) or chars is None or 0 == len(chars):
            return 0
        res, charCounter = 0, Counter(chars)
        for word in words:
            isIncluded = True
            for c, cnt in Counter(word).items():
                if charCounter[c] < cnt:
                    isIncluded = False
                    break
            if isIncluded:
                res += len(word)
        return res


s = Solution()
data = [(["cat","bt","hat","tree"], "atach", 6),
        (["hello","world","leetcode"], "welldonehoneyr", 10),
        ]
for words, chars, expected in data:
    real = s.countCharacters(words, chars)
    print(f'{words}, {chars}, expected {expected}, real {real}, result {expected == real}')
