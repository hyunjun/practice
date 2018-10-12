#   https://leetcode.com/problems/find-and-replace-pattern

#   https://leetcode.com/problems/find-and-replace-pattern/solution


class Solution:
    #   94.41%
    def findAndReplacePattern(self, words, pattern):
        res = []
        for word in words:
            if len(word) != len(pattern):
                continue
            if len(set(word)) != len(set(pattern)):
                continue
            hasMatched, matched = True, {}
            print('{} -> {}'.format(pattern, word))
            for i, p in enumerate(pattern):
                if p in matched:
                    print('compare matched {} vs. word[{}] {}'.format(matched[p], i, word[i]))
                    if matched[p] != word[i]:
                        hasMatched = False
                        break
                else:
                    matched[p] = word[i]
                    print(matched)
            if hasMatched:
                res.append(word)
        return res


s = Solution()
data = [(["abc","deq","mee","aqq","dkd","ccc"], "abb", ["mee","aqq"]),
        ]
for words, pattern, expected in data:
    real = s.findAndReplacePattern(words, pattern)
    print('{}, {}, expected {}, real {}, result {}'.format(words, pattern, expected, real, expected == real))
