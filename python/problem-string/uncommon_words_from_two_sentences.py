#   https://leetcode.com/problems/uncommon-words-from-two-sentences

#   https://leetcode.com/problems/uncommon-words-from-two-sentences/solution


class Solution:
    #   63.44%
    def uncommonFromSentences(self, A, B):
        if (A is None or 0 == len(A)) and (B is None or 0 == len(B)):
            return []
        words = A.split(' ')
        words.extend(B.split(' '))
        wordCntDict = {}
        for word in words:
            if word in wordCntDict:
                wordCntDict[word] += 1
            else:
                wordCntDict[word] = 1
        return [word for word, cnt in wordCntDict.items() if 1 == cnt]


s = Solution()
data = [('this apple is sweet', 'this apple is sour', ['sweet', 'sour']),
        ('apple apple', 'banana', ['banana']),
        ]
for A, B, expected in data:
    real = s.uncommonFromSentences(A, B)
    print('{}, {}, expected {}, real {}, result {}'.format(A, B, expected, real, expected == real))
