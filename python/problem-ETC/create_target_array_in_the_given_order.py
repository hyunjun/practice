#   https://leetcode.com/problems/create-target-array-in-the-given-order


from collections import defaultdict
from typing import List


class Solution:
    #   runtime; 36ms, 37.72%
    #   memory; 12.9MB, 100.00%
    def createTargetArray0(self, nums: List[int], index: List[int]) -> List[int]:
        if nums is None or not (1 <= len(nums) <= 100):
            return []
        target = []
        for i, n in enumerate(nums):
            if len(target) <= index[i]:
                target.append(n)
            else:
                target.insert(index[i], n)
        return target

    #   Wrong Answer
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        if nums is None or not (1 <= len(nums) <= 100):
            return []
        d = defaultdict(list)
        for i, n in enumerate(nums):
            d[index[i]].append(n)
        target = []
        for i in range(max(index) + 1):
            target.extend(d[i][::-1])
        return target


s = Solution()
data = [([0, 1, 2, 3, 4], [0, 1, 2, 2, 1], [0, 4, 1, 3, 2]),
        ([1, 2, 3, 4, 0], [0, 1, 2, 3, 0], [0, 1, 2, 3, 4]),
        ([4, 2, 4, 3, 2], [0, 0, 1, 3, 1], [2, 2, 4, 4, 3]),
        ]
for nums, index, expected in data:
    real = s.createTargetArray(nums, index)
    print(f'{nums} {index} expected {expected} real {real} result {expected == real}')
