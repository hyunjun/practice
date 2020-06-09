#   https://leetcode.com/problems/the-k-strongest-values-in-an-array

#   https://leetcode.com/problems/the-k-strongest-values-in-an-array/discuss/674346/Learn-randomized-algorithm-today-which-solves-this-problem-in-O(n).


from typing import List


class Solution:
    #   runtime; 1812ms, 44.23%
    #   memory; 35.3MB, 100.00%
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        if arr is None or not (1 <= len(arr) <= 10 ** 5) or not (1 <= k <= len(arr)):
            return []
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        return sorted(arr, key=lambda t: (-abs(t - median), -t))[:k]


s = Solution()
data = [([1,2,3,4,5], 2, [5,1]),
        ([1,1,3,5,5], 2, [5,5]),
        ([6,7,11,7,6,8], 5, [11,8,6,6,7]),
        ([6,-3,7,2,11], 3, [-3,11,2]),
        ([-7,22,17,3], 2, [22,17]),
        ]
for arr, k, expect in data:
    real = s.getStrongest(arr, k)
    print(f'{arr} {k} expect {expect} real {real} result {expect == real}')
