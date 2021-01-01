#   https://leetcode.com/problems/check-array-formation-through-concatenation


from typing import List


class Solution:
    #   https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3589
    #   runtime; 40ms, 72.47%
    #   memory; 14.4MB
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        target = ' '.join(f'<{a}>' for a in arr)
        s, indices = [' '.join(f'<{p}>' for p in piece) for piece in pieces], []
        for i, item in enumerate(s):
            if item not in target:
                return False
            indices.append((i, target.index(item)))
        return len(indices) == len(s) and target == ' '.join(s[index[0]] for index in sorted(indices, key=lambda t: t[1]))


s = Solution()
data = [([85], [[85]], True),
        ([15,88], [[88],[15]], True),
        ([49,18,16], [[16,18,49]], False),
        ([91,4,64,78], [[78],[4,64],[91]], True),
        ([1,3,5,7], [[2,4,6,8]], False),
        ([32,66,73,15,3,70,53], [[66,73],[15],[3],[32],[70],[53]], True),
        ]
for arr, pieces, expect in data:
    real = s.canFormArray(arr, pieces)
    print(f'{arr} {pieces} expect {expect} real {real} result {expect == real}')
