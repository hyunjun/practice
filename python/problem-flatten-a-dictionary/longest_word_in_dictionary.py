#   https://leetcode.com/problems/longest-word-in-dictionary

#   https://leetcode.com/problems/longest-word-in-dictionary/solution


class Solution:
    #   Wrong Answer
    def longestWord0(self, words):
        if words is None or 0 == len(words):
            return ''
        cWIdxDict = {}
        for i, word in enumerate(words):
            for c in word:
                if c in cWIdxDict:
                    cWIdxDict[c].add(i)
                else:
                    cWIdxDict[c] = set([i])

        for c, wIdx in sorted(cWIdxDict.items(), key=lambda t: len(t[1])):
            print(c, wIdx)
        def isValid(word):
            usedSet = set()
            for c, wIdx in sorted(cWIdxDict.items(), key=lambda t: len(t[1])):
                if c not in word:
                    continue
                checked = False
                for i in wIdx:
                    if i in usedSet:
                        continue
                    usedSet.add(i)
                    checked = True
                    break
                if not checked:
                    return False
            return True

        for word in sorted(words, key=lambda w: (-len(w), w)):
            if isValid(word):
                return word
        return ''

    #   63.44%
    def longestWord(self, words):
        if words is None or 0 == len(words):
            return ''
        trie = {}
        for word in words:
            if word[0] in trie:
                trie[word[0]].add(word[1:])
            else:
                trie[word[0]] = set([word[1:]])

        def isValid(word):
            if '' not in trie[word[0]]:
                return False
            for i in range(2, len(word)):
                if word[1:i] not in trie[word[0]]:
                    return False
            return True

        for word in sorted(words, key=lambda w: (-len(w), w)):
            if isValid(word):
                return word
        return ''


s = Solution()
data = [(['w', 'wo', 'wor', 'worl', 'world'], 'world'),
        (['a', 'banana', 'app', 'appl', 'ap', 'apply', 'apple'], 'apple'),
        (['yo', 'ew', 'fc', 'zrc', 'yodn', 'fcm', 'qm', 'qmo', 'fcmz', 'z', 'ewq', 'yod', 'ewqz', 'y'], 'yodn'),
        ]
for words, expected in data:
    real = s.longestWord(words)
    print('{}, expected {}, real {}, result {}'.format(words, expected, real, expected == real))
