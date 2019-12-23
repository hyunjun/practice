#   https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array

#   https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/discuss/456394/Randomized-O(logN)-timeO(1)-space-solution


from typing import List


class Solution:
    #   runtime; 116ms, 8.24%
    #   memory; 14.1MB, 100.00%
    def findSpecialInteger0(self, arr: List[int]) -> int:
        if arr is None or not (1 <= len(arr) <= 10 ** 4):
            return None
        maxNum, maxCnt, d = arr[0], 0, {}
        for a in arr:
            if a in d:
                d[a] += 1
            else:
                d[a] = 1
            if maxCnt < d[a]:
                maxNum, maxCnt = a, d[a]
        return maxNum

    #   runtime; 88ms, 92.68%
    #   memory; 14MB, 100.00%
    def findSpecialInteger(self, arr: List[int]) -> int:
        if arr is None or not (1 <= len(arr) <= 10 ** 4):
            return None
        maxNum, maxCnt, d, limit = arr[0], 0, {}, len(arr) // 4 + 1
        for a in arr:
            if a in d:
                d[a] += 1
            else:
                d[a] = 1
            if maxCnt < d[a]:
                maxNum, maxCnt = a, d[a]
                if limit <= maxCnt:
                    return maxNum
        return maxNum


s = Solution()
data = [([1, 2, 2, 6, 6, 6, 6, 7, 10], 6),
        ([1, 2, 2, 2, 6, 6, 6, 6, 10], 6),
        ([2, 2, 2, 2, 6, 6, 6, 7, 10], 2),
        ([1, 2, 2, 6, 6, 7, 7, 7, 7], 7),
        ([2, 2, 2, 6, 6, 6, 6, 6, 7], 6),
        ]
for arr, expected in data:
    real = s.findSpecialInteger(arr)
    print(f'{arr} expected {expected} real {real} result {expected == real}')
