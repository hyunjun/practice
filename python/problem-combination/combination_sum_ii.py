#   https://leetcode.com/problems/combination-sum-ii


from typing import List


class Solution:
    #   runtime; 264ms, 19.99%
    #   memory; 13.9MB, 54.41%
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        self.res = set()
        def getSum(cands, acc, curSum):
            for i, c in enumerate(cands):
                if 0 < len(acc) and c < acc[-1]:
                    continue
                if curSum + c <= target:
                    acc.append(c)
                    if curSum + c == target:
                        self.res.add(tuple(acc[:]))
                    else:
                        getSum(cands[i + 1:], acc, curSum + c)
                    acc.pop()
        getSum(candidates, [], 0)

        return [list(r) for r in self.res]


s = Solution()
data = [([10, 1, 2, 7, 6, 1, 5], 8, [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]),
        ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
        ]
for candidates, target, expect in data:
    real = s.combinationSum2(candidates, target)
    print(f'{candidates} {target} expect {expect} real {real} result {sorted(expect) == sorted(real)}')
