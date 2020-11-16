#   https://leetcode.com/problems/longest-mountain-in-array


from typing import List


class Solution:
    #   https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3533
    #   runtime; 164ms, 73.88%
    #   memory; 15MB
    def longestMountain(self, A: List[int]) -> int:
        maxLen = 0
        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i] > A[i + 1]:
                l, r = i - 1, i + 1
                while 0 < l and A[l - 1] < A[l]:
                    l -= 1
                while r < len(A) - 1 and A[r] > A[r + 1]:
                    r += 1
                maxLen = max(maxLen, r - l + 1)
        return maxLen


s = Solution()
data = [([2,1,4,7,3,2,5], 5),
        ([2,2,2], 0),
        ([40,51,29,19,50,25], 4),
        ]
for A, expect in data:
    real = s.longestMountain(A)
    print(f'{A} expect {expect} real {real} result {expect == real}')
