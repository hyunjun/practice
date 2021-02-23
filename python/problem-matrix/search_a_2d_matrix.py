#   https://leetcode.com/problems/search-a-2d-matrix


from typing import List


class Solution:
    #   https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3497
    #   runtime; 36ms, 99.08%
    #   memory; 14.5MB
    def searchMatrix0(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(arr):
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if arr[m] == target:
                    return m
                elif arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        if target < matrix[0][0] or matrix[-1][-1] < target:
            return False

        R, C, minRow, maxRow = len(matrix), len(matrix[0]), 0, 0
        for r in range(1, R):
            if matrix[r - 1][0] <= target < matrix[r][0]:
                minRow = r - 1
                break
        for r in range(1, R):
            if matrix[r - 1][-1] < target <= matrix[r][-1]:
                maxRow = r
                break
        for r in range(minRow, maxRow + 1):
            idx = binarySearch(matrix[r])
            if idx != -1:
                return True
        return False

    #   https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3650
    #   runtime; 216ms, 15.54%
    #   memory; 20.6MB, 68.22%
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == target:
                    return True
        return False

    #   runtime; 168ms, 52.23%
    #   memory; 20.5MB, 89.49%
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])

        def bSearch(arr):
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if arr[m] == target:
                    return (True, m)
                if arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return (False, m if target < arr[m] else m + 1)

        isMatched, maxCol = bSearch(matrix[0])
        if isMatched:
            return True
        isMatched, maxRow = bSearch([matrix[r][0] for r in range(R)])
        if isMatched:
            return True
        for r in range(maxRow):
            if bSearch([matrix[r][c] for c in range(maxCol)])[0]:
                return True
        return False


s = Solution()
data = [([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3, True),
        ([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 16, True),
        ([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 23, True),
        ([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 6, False),
        ([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13, False),
        ([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 39, False),
        ]
for matrix, target, expect in data:
    for m in matrix:
        print(m)
    real = s.searchMatrix(matrix, target)
    print(f'expect {expect} real {real} result {expect == real}')
'''
binary search로 col[0]과 col[-1]을 검색해서 maxRow와 minRow를 찾고
다시 해당 row에 대해 binary search로 일치하는 값이 있는지 검사
O(log(R) * 2 + (maxRow - minRow) * log(C))
'''
