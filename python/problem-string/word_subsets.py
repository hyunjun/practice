#   https://leetcode.com/problems/word-subsets

#   https://leetcode.com/problems/word-subsets/solution


from collections import Counter
from typing import List


class Solution:
    #   https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3685
    def wordSubsets0(self, A: List[str], B: List[str]) -> List[str]:

        def isIncluded(a, b):
            for c, cnt in a.items():
                if c not in b or b[c] < cnt:
                    return False
            return True

        res, aList, bList = [], [(a, Counter(a)) for a in A], [Counter(b) for b in B]
        for word, c in aList:
            if all(isIncluded(b, c) for b in bList):
                res.append(word)
        return res

    #   runtime; 948ms, 47.49%
    #   memory; 22.5MB, 5.59%
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        def isIncluded(a, b):
            for c, cnt in a.items():
                if c not in b or b[c] < cnt:
                    return False
            return True

        res, aList, bCntDict = [], [(a, Counter(a)) for a in A], Counter()
        for b in B:
            for c, cnt in Counter(b).items():
                bCntDict[c] = max(cnt, bCntDict[c])
        for word, c in aList:
            if isIncluded(bCntDict, c):
                res.append(word)
        return res


s = Solution()
data = [(["amazon","apple","facebook","google","leetcode"], ["e","o"], ["facebook","google","leetcode"]),
        (["amazon","apple","facebook","google","leetcode"], ["l","e"], ["apple","google","leetcode"]),
        (["amazon","apple","facebook","google","leetcode"], ["e","oo"], ["facebook","google"]),
        (["amazon","apple","facebook","google","leetcode"], ["lo","eo"], ["google","leetcode"]),
        (["amazon","apple","facebook","google","leetcode"], ["ec","oc","ceo"], ["facebook","leetcode"]),
        ]
for A, B, expect in data:
    real = s.wordSubsets(A, B)
    print(f'{A} {B} expect {expect} real {real} result {expect == real}')
