#   https://leetcode.com/problems/summary-ranges


from typing import List


class Solution:
    #   https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3510
    #   runtime; 20ms, 98.08%
    #   memory; 14.3MB
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums is None or 0 == len(nums):
            return []
        res, idx = [], 0
        for i, n in enumerate(nums):
            res.append(idx)
            if 0 < i and nums[i - 1] == n - 1:
                res[i] = res[i - 1]
            idx += 1
        d = {}
        for i, n in enumerate(nums):
            if res[i] not in d:
                d[res[i]] = [n, n]
            else:
                d[res[i]][1] = n
        return [str(minVal) if minVal == maxVal else f'{minVal}->{maxVal}' for n, (minVal, maxVal) in sorted(d.items())]


s = Solution()
data = [([0,1,2,4,5,7], ["0->2","4->5","7"]),
        ([0,2,3,4,6,8,9], ["0","2->4","6","8->9"]),
        ([], []),
        ([-1], ["-1"]),
        ([0], ["0"]),
        ]
for nums, expect in data:
    real = s.summaryRanges(nums)
    print(f'{nums} expect {expect} real {real} result {expect == real}')
