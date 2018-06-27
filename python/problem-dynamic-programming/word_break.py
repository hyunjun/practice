#   https://leetcode.com/problems/word-break

#   https://leetcode.com/problems/word-break/discuss/140641/Python-short-DP-code
#   https://leetcode.com/problems/word-break/discuss/141492/Python-backtracking-with-pruning-93


#from collections import defaultdict
#INF_DICT = lambda: defaultdict(INF_DICT)


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
    def wordBreak(self, s, wordDict):
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
        print('{}, {}, expected {}, real {}, result {}'.format(s, wordDict, expected, real, expected == real))
    else:
        print('{}..., {}, expected {}, real {}, result {}'.format(s[:10], wordDict, expected, real, expected == real))
