#   https://leetcode.com/problems/combination-sum


from typing import List


class Solution:
    #   runtime; 96ms, 50.51%
    #   memory; 14MB, 26.21%
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.res = []
        def getSum(acc, curSum):
            for c in candidates:
                if 0 < len(acc) and c < acc[-1]:
                    continue
                if curSum + c <= target:
                    acc.append(c)
                    if curSum + c == target:
                        self.res.append(acc[:])
                    else:
                        getSum(acc, curSum + c)
                    acc.pop()
        getSum([], 0)

        return self.res


s = Solution()
data = [([2, 3, 6, 7], 7, [[7], [2, 2, 3]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ]
for candidates, target, expect in data:
    real = s.combinationSum(candidates, target)
    print(f'{candidates} {target} expect {expect} real {real} result {sorted(expect) == sorted(real)}')
