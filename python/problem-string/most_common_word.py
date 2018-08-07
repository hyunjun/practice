#   https://leetcode.com/problems/most-common-word

#   https://leetcode.com/problems/most-common-word/solution


class Solution:
    #   50.63%
    def mostCommonWord(self, paragraph, banned):
        d = {}
        for word in paragraph.split():
            w = ''.join([c for c in word.lower() if 'a' <= c <= 'z'])
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        for w, cnt in sorted(d.items(), key=lambda t: t[1], reverse=True):
            if w in set(banned):
                continue
            return w
        return None


s = Solution()
data = [('Bob hit a ball, the hit BALL flew far after it was hit.', ['hit'], 'ball'),
        ]
for paragraph, banned, expected in data:
    real = s.mostCommonWord(paragraph, banned)
    print('{}, {}, expected {}, real {}, result {}'.format(paragraph, banned, expected, real, expected == real))
