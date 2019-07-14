#   https://leetcode.com/problems/relative-sort-array


from typing import List
from collections import Counter


class Solution:
    #   runtime; 36ms, 50.00%
    #   memory; 13.3MB, 100.00%
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if arr1 is None or 0 == len(arr1) or arr2 is None or 0 == len(arr2):
            return arr1
        s, arr1Only = set(arr2), []
        for a in arr1:
            if a not in s:
                arr1Only.append(a)
        res, c = [], Counter(arr1)
        for a in arr2:
            for _ in range(c[a]):
                res.append(a)
        res.extend(sorted(arr1Only))
        return res


s = Solution()
data = [([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6], [2,2,2,1,4,3,3,9,6,7,19]),
        ]
for arr1, arr2, expected in data:
    real = s.relativeSortArray(arr1, arr2)
    print(f'{arr1}, {arr2}, expected {expected}, real {real}, result {expected == real}')
