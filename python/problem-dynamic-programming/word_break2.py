#   https://leetcode.com/problems/word-break-ii

#   https://leetcode.com/problems/word-break-ii/discuss/158736/DP-+-Backtracking-clean-python-solution


from collections import defaultdict


class Solution:
    #   Time Limit Exceeded
    def wordBreak0(self, s, wordDict):
        res, wordSet = [], set(wordDict)
        def hasWordsInDict(prev, rest):
            if 0 == len(rest):
                res.append(' '.join(prev))
            else:
                if rest in wordSet:
                    prev.append(rest)
                    hasWordsInDict(prev, '')
                    prev.pop()
                for i in range(1, len(rest)):
                    if rest[:i] in wordSet:
                        prev.append(rest[:i])
                        hasWordsInDict(prev, rest[i:])
                        prev.pop()
        hasWordsInDict([], s)
        return res

    #   Time Limit Exceeded
    def wordBreak1(self, s, wordDict):
        dp = [None] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                sIdx = i - len(word) + 1
                if sIdx < 0 or s[sIdx:i + 1] != word:
                    continue
                if dp[i]:
                    dp[i].append((sIdx, i))
                else:
                    dp[i] = [(sIdx, i)]
        res, q = [], [([], sIdx, eIdx) for sIdx, eIdx in dp[-1]]
        while q:
            prev, sIdx, eIdx = q.pop(0)
            if 0 == sIdx:
                prev.append(s[sIdx:eIdx + 1])
                res.append(' '.join(prev[::-1]))
            else:
                if dp[sIdx - 1] is None:
                    continue
                for nsIdx, neIdx in dp[sIdx - 1]:
                    prev.append(s[sIdx:eIdx + 1])
                    q.append((prev[::], nsIdx, neIdx))
                    prev.pop()
        return res

    #   Time Limit Exceeded
    def wordBreak2(self, s, wordDict):
        res = []
        def hasWordsInDict(prev, start):
            for word in wordDict:
                if word == s[start:start + len(word)]:
                    prev.append(word)
                    if len(s) <= start + len(word):
                        res.append(' '.join(prev))
                    else:
                        hasWordsInDict(prev, start + len(word))
                    prev.pop()
        hasWordsInDict([], 0)
        return res

    #   Time Limit Exceeded
    def wordBreak3(self, s, wordDict):
        dp = [None] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                sIdx = i - len(word) + 1
                if sIdx < 0 or s[sIdx:i + 1] != word:
                    continue
                if dp[i] is None:
                    dp[i] = []
                if 0 == sIdx:
                    if dp[i]:
                        dp[i].append([0, i + 1])
                    else:
                        dp[i] = [[0, i + 1]]
                if 0 <= sIdx - 1:
                    if dp[sIdx - 1]:
                        for prev in dp[sIdx - 1]:
                            tmp = prev[:]
                            tmp.append(i + 1)
                            dp[i].append(tmp)
        res = []
        for idxList in dp[-1]:
            if 0 == idxList[0] and len(s) == idxList[-1]:
                tmp = []
                for i in range(1, len(idxList)):
                    tmp.append(s[idxList[i - 1]:idxList[i]])
                res.append(' '.join(tmp))
        return res

    #   29.28%
    def wordBreak(self, s, wordDict):
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                sIdx = i - len(word) + 1
                if sIdx < 0 or s[sIdx:i + 1] != word:
                    continue
                if 0 == sIdx or dp[sIdx - 1]:
                    dp[i] = True
        #print(dp[i])
        if False == dp[i]:
            return []
        dp = [None] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                sIdx = i - len(word) + 1
                if sIdx < 0 or s[sIdx:i + 1] != word:
                    continue
                if dp[i] is None:
                    dp[i] = []
                if 0 == sIdx:
                    if dp[i]:
                        dp[i].append([0, i + 1])
                    else:
                        dp[i] = [[0, i + 1]]
                if 0 <= sIdx - 1:
                    if dp[sIdx - 1]:
                        for prev in dp[sIdx - 1]:
                            tmp = prev[:]
                            tmp.append(i + 1)
                            dp[i].append(tmp)
        res = []
        for idxList in dp[-1]:
            if 0 == idxList[0] and len(s) == idxList[-1]:
                tmp = []
                for i in range(1, len(idxList)):
                    tmp.append(s[idxList[i - 1]:idxList[i]])
                res.append(' '.join(tmp))
        return res


solution = Solution()
data = [("catsanddog", ["cat", "cats", "and", "sand", "dog"], ["cats and dog", "cat sand dog"]),
	("catsandog", ["cats", "dog", "sand", "and", "cat"], []),
	("aaa", ["a", "aa", "aaa"], ["a a a", "a aa", "aa a", "aaa"]),
	("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"], ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]),
	("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"], []),
	]
for s, wordDict, expected in data:
    real = solution.wordBreak(s, wordDict)
    print('{}, {}\n\texpected {}, real {}, result {}'.format(s, wordDict, expected, real, sorted(expected) == sorted(real)))
