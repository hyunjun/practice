#   https://leetcode.com/problems/maximum-score-words-formed-by-letters

#   https://leetcode.com/problems/maximum-score-words-formed-by-letters/discuss/436419/Python-solution-backtrack-with-explanation


from collections import Counter


class Solution(object):
    #   Wrong Answer
    def maxScoreWords0(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        def getScore(word):
            return sum([score[ord(c) - ord('a')] for c in word])

        def isIncluded(charCountDict, word):
            for c in word:
                if charCountDict[c] == 0:
                    return False
                charCountDict[c] -= 1
            return True

        _sum, cntDict = 0, Counter(letters)
        for word, score in sorted([(word, getScore(word)) for word in words], key=lambda t: t[1], reverse=True):
            if False == isIncluded(cntDict.copy(), word):
                continue
            for c in word:
                cntDict[c] -= 1
            _sum += score
        return _sum

    #   Time Limit Exceeded
    def maxScoreWords1(self, words, letters, score):

        def getScore(word):
            return sum([score[ord(c) - ord('a')] for c in word])

        def isIncluded(charCountDict, word):
            for c in word:
                if charCountDict[c] == 0:
                    return False
                charCountDict[c] -= 1
            return True

        self._sum, wordScores = 0, sorted([(word, getScore(word)) for word in words], key=lambda t: t[1], reverse=True)

        def getMaxSum(cntDict, wordScores, acc):
            if 0 == len(wordScores):
                return
            for i, (word, score) in enumerate(wordScores):
                if False == isIncluded(cntDict.copy(), word):
                    continue
                for c in word:
                    cntDict[c] -= 1
                acc += score
                self._sum = max(self._sum, acc)
                getMaxSum(cntDict, wordScores[:i] + wordScores[i + 1:], acc)
                for c in word:
                    cntDict[c] += 1
                acc -= score

        getMaxSum(Counter(letters), [(w, s) for w, s in wordScores if 0 < s], 0)

        return self._sum

    #   Time Limit Exceeded
    def maxScoreWords2(self, words, letters, score):

        def getScore(word):
            return sum([score[ord(c) - ord('a')] for c in word])

        def isIncluded(charCountDict, word):
            for c, cnt in word.items():
                if charCountDict[c] < cnt:
                    return False
            return True

        self._sum, wordScores = 0, sorted([(Counter(word), getScore(word)) for word in words], key=lambda t: t[1], reverse=True)

        def getMaxSum(cntDict, wordScores, acc):
            if 0 == len(wordScores):
                return
            for i, (wordCntDict, score) in enumerate(wordScores):
                if False == isIncluded(cntDict, wordCntDict):
                    continue
                acc += score
                self._sum = max(self._sum, acc)
                getMaxSum(cntDict - wordCntDict, wordScores[:i] + wordScores[i + 1:], acc)
                acc -= score

        getMaxSum(Counter(letters), [(w, s) for w, s in wordScores if 0 < s], 0)

        return self._sum

    #   runtime; 124ms, 24.06%
    #   memory; 12.3MB, 100.00%
    def maxScoreWords3(self, words, letters, score):

        def getScore(word):
            return sum([score[ord(c) - ord('a')] for c in word])

        def isIncluded(totalCountDict, wordCountDict):
            for c, cnt in wordCountDict.items():
                if totalCountDict[c] < cnt:
                    return False
            return True

        self._sum, self._memo, wordScores = 0, {}, sorted([(word, Counter(word), getScore(word)) for word in words], key=lambda t: t[2], reverse=True)

        def getMaxSum(cntDict, wordScores, accWordCntDict, acc):
            keywords = ' '.join(sorted([w for w, c in accWordCntDict.items() if 0 < c]))
            if keywords in self._memo:
                return self._memo[keywords]
            subSum = acc
            for i, (word, wordCntDict, score) in enumerate(wordScores):
                if False == isIncluded(cntDict, wordCntDict):
                    continue
                acc += score
                accWordCntDict[word] += 1
                curSum = max(acc, getMaxSum(cntDict - wordCntDict, wordScores[:i] + wordScores[i + 1:], accWordCntDict, acc))
                subSum = max(subSum, curSum)
                acc -= score
                accWordCntDict[word] -= 1
            self._memo[keywords] = subSum
            return subSum

        return getMaxSum(Counter(letters), [(w, wcDict, s) for w, wcDict, s in wordScores if 0 < s], Counter(), 0)

    #   runtime; 52ms, 67.35%
    #   memory; 12MB, 100.00%
    def maxScoreWords(self, words, letters, score):

        def getScore(word):
            return sum([score[ord(c) - ord('a')] for c in word])

        def isIncluded(totalCountDict, wordCountDict):
            for c, cnt in wordCountDict.items():
                if totalCountDict[c] < cnt:
                    return False
            return True

        self._sum, self._memo, wordScores = 0, {}, sorted([(word, Counter(word), getScore(word)) for word in words], key=lambda t: t[2], reverse=True)

        def getMaxSum(cntDict, wordScores, accWordCntDict, acc):
            candidates = [(word, wordCntDict, score) for word, wordCntDict, score in wordScores if isIncluded(cntDict, wordCntDict)]

            keywordSet = set([w for w, c in accWordCntDict.items() if 0 < c])
            [keywordSet.add(w) for w, _, _ in candidates]
            keywords = ' '.join(sorted(keywordSet))
            if keywords in self._memo:
                return self._memo[keywords]

            subSum = acc
            for i, (word, wordCntDict, score) in enumerate(candidates):
                acc += score
                accWordCntDict[word] += 1
                curSum = max(acc, getMaxSum(cntDict - wordCntDict, candidates[:i] + candidates[i + 1:], accWordCntDict, acc))
                subSum = max(subSum, curSum)
                acc -= score
                accWordCntDict[word] -= 1
            self._memo[keywords] = subSum
            return subSum

        return getMaxSum(Counter(letters), [(w, wcDict, s) for w, wcDict, s in wordScores if 0 < s], Counter(), 0)


s = Solution()
data = [(["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0], 23),
        (["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10], 27),
        (["leetcode"], ["l","e","t","c","o","d"], [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0], 0),
        (["daeagfh","acchggghfg","feggd","fhdch","dbgadcchfg","b","db","fgchfe","baaedddc"], ["a","a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","d","d","d","d","d","d","d","d","d","d","d","d","d","d","e","e","e","e","e","e","e","e","e","e","f","f","f","f","f","f","f","f","f","f","f","f","f","f","g","g","g","g","g","g","g","g","g","g","g","g","h","h","h","h","h","h","h","h","h","h","h","h","h"], [2,1,9,2,10,5,7,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 298),
        (["e","bac","baeba","eb","bbbbd","cad","c","c"], ["a","a","a","a","a","a","a","b","b","b","b","b","b","c","c","c","c","c","c","d","d","d","d","d","d","d","e","e","e","e"], [8,4,6,8,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 95),
        (["dbccbcb","bdacbae","eaa","aeccedc","ecaeaa","ebeec","abcb"], ["a","a","a","a","b","b","b","b","b","b","b","c","c","d","d","d","d","d","d","e","e","e","e"], [4,10,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 70),
        ]
for words, letters, score, expected in data:
    real = s.maxScoreWords(words, letters, score)
    print(f'{words}, {letters}, {score}, expected {expected}, real {real}, result {expected == real}')
