#   https://leetcode.com/problems/combination-sum-iii


from typing import List


class Solution:
    #   https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3457
    #   runtime; 28ms, 88.28%
    #   memory; 13.7MB, 85.69%
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        self.res = []
        def getSum(acc):
            if len(acc) == k - 1:
                cand = n - sum(acc)
                if acc[-1] < cand <= 9:
                    acc.append(cand)
                    self.res.append(acc[:])
                    acc.pop()
            else:
                s = 1 if len(acc) == 0 else acc[-1] + 1
                for i in range(s, 9):
                    acc.append(i)
                    getSum(acc)
                    acc.pop()
        getSum([])

        return self.res



s = Solution()
data = [(3, 7, [[1, 2, 4]]),
        (3, 9, [[1, 2, 6], [1, 3, 5], [2, 3, 4]]),
        (2, 18, []),
        (4, 24, [[1,6,8,9],[2,5,8,9],[2,6,7,9],[3,4,8,9],[3,5,7,9],[3,6,7,8],[4,5,6,9],[4,5,7,8]]),
        ]
for k, n, expect in data:
    real = s.combinationSum3(k, n)
    print(f'{k} {n} expect {expect} real {real} result {expect == real}')
