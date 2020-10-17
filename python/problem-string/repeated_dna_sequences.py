#   https://leetcode.com/problems/repeated-dna-sequences


from collections import defaultdict
from typing import List


class Solution:
    #   Time Limit Exceeded
    def findRepeatedDnaSequences0(self, s: str) -> List[str]:
        res, added = [], set()
        for i in range(len(s) - 10):
            subStr = s[i:i + 10]
            if subStr in added:
                continue
            if subStr in s[i + 1:]:
                res.append(subStr)
                added.add(subStr)
        return res

    #   https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3498
    #   runtime; 96ms, 18.74%
    #   memory; 38.7MB
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = defaultdict(list)
        for i in range(len(s) - 9):
            d[s[i:i + 10]].append(i)
        return [subStr for subStr, _ in sorted([(subStr, idxList[0]) for subStr, idxList in d.items() if 1 < len(idxList)], key=lambda t: t[1])]


solution = Solution()
data = [("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["AAAAACCCCC","CCCCCAAAAA"]),
        ("AAAAAAAAAAAAA", ["AAAAAAAAAA"]),
        ("AAAAAAAAAAA", ["AAAAAAAAAA"]),
        ]
for s, expect in data:
    real = solution.findRepeatedDnaSequences(s)
    print(f'{s} expect {expect} real {real} result {expect == real}')
