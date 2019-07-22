#   https://leetcode.com/problems/number-of-equivalent-domino-pairs

#   https://leetcode.com/problems/number-of-equivalent-domino-pairs/discuss/340022/JavaC%2B%2BPython-Easy-and-Concise


from collections import defaultdict
from typing import List


class Solution:
    #   runtime; 272ms, 25.00%
    #   memory; 23.5MB, 100.00%
    def numEquivDominoPairs0(self, dominoes: List[List[int]]) -> int:
        if dominoes is None or 0 == len(dominoes):
            return 0
        d = defaultdict(int)
        for domino in dominoes:
            d[tuple(sorted(domino))] += 1
        res = 0
        for k, cnt in d.items():
            if 1 < cnt:
                res += cnt * (cnt - 1) // 2
        return res

    #   runtime; 288ms, 25.00%
    #   memory; 23.4MB, 100.00%
    def numEquivDominoPairs1(self, dominoes: List[List[int]]) -> int:
        if dominoes is None or 0 == len(dominoes):
            return 0
        cntDict, resDict = defaultdict(int), defaultdict(int)
        for domino in dominoes:
            key = tuple(sorted(domino))
            cntDict[key] += 1
            resDict[key] = cntDict[key] * (cntDict[key] - 1) // 2
        return sum(resDict.values())

    #   runtime; 256ms, 25.00%
    #   memory; 23.1MB, 100.00%
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        if dominoes is None or 0 == len(dominoes):
            return 0
        tupledDominoes = [tuple(sorted(domino)) for domino in dominoes]
        d = defaultdict(int)
        for domino in tupledDominoes:
            d[domino] += 1
        res = 0
        for _, cnt in d.items():
            if 1 < cnt:
                res += cnt * (cnt - 1) // 2
        return res


s = Solution()
data = [([[1,2],[2,1],[3,4],[5,6]], 1),
        ([[1,2],[2,1],[3,4],[5,6], [4, 3], [6, 5], [9, 4], [2, 1]], 5),
        ]
for dominoes, expected in data:
    real = s.numEquivDominoPairs(dominoes)
    print(f'{dominoes}, expected {expected}, real {real}, result {expected == real}')
