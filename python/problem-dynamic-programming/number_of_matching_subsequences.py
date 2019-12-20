#   https://leetcode.com/problems/number-of-matching-subsequences


from typing import List


class Solution:
    #   runtime; 1704ms, 9.56%
    #   memory; 14MB, 100.00%
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        if S is None or 0 == len(S) or words is None or 0 == len(words):
            return 0

        d = {}
        def isSubsequence(seq, cand):
            if cand in d:
                return d[cand]
            i, candLen = 0, len(cand)
            for s in seq:
                if s == cand[i]:
                    i += 1
                if i == candLen:
                    d[cand] = True
                    return True
            res = i == candLen
            d[cand] = res
            return res

        return sum(1 if isSubsequence(S, word) else 0 for word in words)


s = Solution()
data = [('abcde', ['a', 'bb', 'acd', 'ace'], 3),
        ("qlhxagxdqh", ["qlhxagxdq","qlhxagxdq","lhyiftwtut","yfzwraahab"], 2),
        ]
for S, words, expected in data:
    real = s.numMatchingSubseq(S, words)
    print(f'{S} {words} expected {expected} real {real} result {expected == real}')
