#   https://leetcode.com/problems/word-break

#   https://leetcode.com/problems/word-break/discuss/140641/Python-short-DP-code
#   https://leetcode.com/problems/word-break/discuss/141492/Python-backtracking-with-pruning-93


from collections import defaultdict
from typing import List


INF_DICT = lambda: defaultdict(INF_DICT)


class Solution:

    #   Time Limit Exceeded
    def wordBreak0(self, s, wordDict):
        if s is None or 0 == len(s) or wordDict is None or 0 == len(wordDict):
            return False
        sSet = set(s)
        wordSet = set()
        for word in wordDict:
            for w in word:
                wordSet.add(w)
        if 0 < len(sSet - wordSet):
            return False

        #print()
        if set(s).difference(set(''.join(wordDict))) != set():
            return False

        wordDict = sorted(wordDict, key=lambda w: len(w), reverse=True)

        def hasWord(word):
            if 0 == len(word):
                return True
            #print('word {}'.format(word))
            for w in wordDict:
                if w in word:
                    idx = word.index(w)
                    if idx == 0:
                        result = hasWord(word[idx + len(w):])
                        if result:
                            return True
            return False

        return hasWord(s)

    #   Wrong Answer
    def wordBreak1(self, s, wordDict):
        if s is None or 0 == len(s) or wordDict is None or 0 == len(wordDict):
            return False
        sSet = set(s)
        wordSet = set()
        for word in wordDict:
            for w in word:
                wordSet.add(w)
        if 0 < len(sSet - wordSet):
            return False

        trie = INF_DICT()
        for word in wordDict:
            n = trie
            for c in word:
                n = n[c]
            n['$'] = 1
        #print(trie)
        #print(trie['a']['a']['a'])
        #print(trie['a']['a']['a']['a'])

        n = trie
        for i, c in enumerate(s):
            if c in n:
                n = n[c]
                #print('[{}]{} {}'.format(i, c, n.keys()))
                if '$' in n and n['$'] == 1:
                    #print('end of dict word')
                    if i != len(s) - 1 and 1 == len(n):
                        n = trie
            else:
                break
        print('"$" in n {}'.format('$' in n))
        if i == len(s) - 1 and '$' in n and n['$'] == 1:
            return True

        def hasWord(w):
            if 0 == len(w):
                return True
            #print('w {}[{}]'.format(w, len(w)))
            for i in range(len(w)):
                cand = w[:i + 1]
                #print('\t[{}]cand {}'.format(i + 1, cand))
                if cand in wordDict:
                    result = hasWord(w[i + 1:])
                    if result:
                        return result
            return False

        return hasWord(s)

    #   94.16%
    #   dynamic programming
    def wordBreak2(self, s, wordDict):
        if s is None or 0 == len(s) or wordDict is None or 0 == len(wordDict):
            return False

        sSet, wordSet = set(s), set()
        for word in wordDict:
            for w in word:
                wordSet.add(w)
        #   if string 's' has character(s) which does NOT exist in all characters in 'wordDict'
        if 0 < len(sSet - wordSet):
            return False

        counts = [0] * len(s)
        for i, c in enumerate(s):
            for word in wordDict:
                start = i - (len(word) - 1)
                start = 0 if start < 0 else start
                #print(word, start, i, s[start:i + 1])
                if s[start:i + 1] == word:
                    if (0 <= start - 1 and 1 == counts[start - 1]) or start - 1 < 0:
                        counts[i] = 1
        #print(counts)
        return 0 < counts[-1]

    #   https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/558/week-5-september-29th-september-30th/3477
    #   Time Limit Exceeded
    def wordBreak3(self, s: str, wordDict: List[str]) -> bool:
        
        t = lambda: defaultdict(t)
        trie = t()
        
        for word in wordDict:
            _trie = trie
            for c in word:
                _trie = _trie[c]
            _trie['$'] = True
            
        def isIncluded(subStr):
            _trie = trie
            for c in subStr:
                if c not in _trie:
                    return False
                _trie = _trie[c]
            return '$' in _trie and _trie['$'] == True
        
        def consume(subStr):
            if 0 == len(subStr):
                return True
            for i in range(1, len(subStr) + 1):
                if isIncluded(subStr[:i]):
                    if consume(subStr[i:]):
                        return True
            return False
        
        return consume(s)

    #   runtime; 40ms, 71.18%
    #   memory; 14.3MB, 6.73%
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(dp)):
            for word in wordDict:
                if dp[i - 1] and s[i - 1:i - 1 + len(word)] == word:
                    dp[i - 1 + len(word)] = True
        return dp[-1]


solution = Solution()
data = [('leecode', ['leet', 'code'], False),
        ('leetcode', ['leet', 'code'], True),
        ('leetcod', ['leet', 'code'], False),
        ('leetcode', ['leet', 'cod'], False),
        ("aaaaaaa", ["aaaa","aaa"], True),
        ("bb", ["a","b","bbb","bbbb"], True),
        ("abcd", ["a","abc","b","cd"], True),
        ("ccbb", ["bc","cb"], False),
        ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"], False),
        ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"], False),
        ]
for s, wordDict, expected in data:
    real = solution.wordBreak(s, wordDict)
    if len(s) < 10:
        print(f'{s}, {wordDict}, expected {expected}, real {real}, result {expected == real}')
    else:
        print(f'{s[:10]}..., {wordDict}, expected {expected}, real {real}, result {expected == real}')
