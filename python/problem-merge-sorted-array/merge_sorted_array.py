

from typing import List


class Solution:
    #   https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3600
    #   runtime; 44ms, 13.84%
    #   memory; 14.1MB, 82.23%
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if nums1 is None or 0 == len(nums1) or m == 0:
            nums1[:] = nums2
        if nums2 is None or 0 == len(nums2) or n == 0:
            return
        fromIdx, toIdx = m - 1, len(nums1) - 1
        while 0 <= fromIdx:
            nums1[toIdx] = nums1[fromIdx]
            fromIdx -= 1
            toIdx -= 1
        idx, i, j = 0, len(nums1) - m, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums1[idx] = nums1[i]
                i += 1
            else:
                nums1[idx] = nums2[j]
                j += 1
            idx += 1
        while i < len(nums1):
            nums1[idx] = nums1[i]
            i += 1
            idx += 1
        while j < len(nums2):
            nums1[idx] = nums2[j]
            j += 1
            idx += 1


s = Solution()
data = [([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
        ([1], 1, [], 0, [1]),
        ([1,2,3,9,0,0,0], 4, [2,5,6], 3, [1, 2, 2, 3, 5, 6, 9]),
        ([0], 0, [1], 1, [1]),
        ]
for nums1, m, nums2, n, expect in data:
    print(f'{nums1} {m} {nums2} {n}')
    s.merge(nums1, m, nums2, n)
    print(f'\t{nums1} {expect} {nums1 == expect}')
