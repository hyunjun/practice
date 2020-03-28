#   https://leetcode.com/problems/find-the-distance-value-between-two-arrays


from typing import List


class Solution:
    #   runtime; 116ms, 46.24%
    #   memory; 13.9MB, 100.00%
    def findTheDistanceValue0(self, arr1: List[int], arr2: List[int], d: int) -> int:
        if arr1 is None or arr2 is None or not (1 <= len(arr1) <= 500) or not (1 <= len(arr2) <= 500):
            return 0
        cnt = 0
        for a1 in arr1:
            if all(abs(a1 - a2) > d for a2 in arr2):
                cnt += 1
        return cnt

    #   runtime; 96ms, 78.89%
    #   memory; 13.9MB, 100.00%
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        if arr1 is None or arr2 is None or not (1 <= len(arr1) <= 500) or not (1 <= len(arr2) <= 500):
            return 0
        numDict, result = {}, {}
        for a in arr1:
            if a not in numDict:
                numDict[a] = [0, 0]
            numDict[a][0] += 1
            result[a] = [False, False]
        l2, r2 = arr2[0], arr2[0]
        for a in arr2:
            if a not in numDict:
                numDict[a] = [0, 0]
            numDict[a][1] += 1
            if a < l2:
                a = l2
            if r2 < a:
                a = r2
        nums = sorted(numDict.keys())
        for n in nums:
            if numDict[n][1] > 0:
                l2 = n
            if numDict[n][0] > 0:
                if abs(n - l2) > d:
                    result[n][0] = True
        for n in nums[::-1]:
            if numDict[n][1] > 0:
                r2 = n
            if numDict[n][0] > 0:
                if abs(r2 - n) > d:
                    result[n][1] = True
        cnt = 0
        for a in arr1:
            if result[a][0] and result[a][1]:
                cnt += 1
        return cnt


s = Solution()
data = [([4, 5, 8], [10, 9, 1, 8], 2, 2),
        ([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3, 2),
        ([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6, 1),
        ([-3, -3, 4, -1, -10], [7, 10], 12, 1),
        ([-3, 10, 2, 8, 0, 10], [-9, -1, -4, -9, -8], 9, 2),
        ]
for arr1, arr2, d, expected in data:
    real = s.findTheDistanceValue(arr1, arr2, d)
    print(f'{arr1} {arr2} {d} expected {expected} real {real} result {expected == real}')

'''
          -3     0  2   8    10
-9 -8 -4      -1
'''
