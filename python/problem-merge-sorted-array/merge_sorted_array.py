#   https://leetcode.com/problems/merge-sorted-array
#   97.69%


class Solution:
    def merge(self, nums1, m, nums2, n):
        if nums1 is None or 0 == len(nums1) or nums2 is None or 0 == len(nums2):
            return None

        rIdx, idx1, idx2 = m + n - 1, m - 1, n - 1
        while 0 <= idx1 and 0 <= idx2:
            if nums1[idx1] < nums2[idx2]:
                nums1[rIdx] = nums2[idx2]
                idx2 -= 1
            else:
                nums1[rIdx] = nums1[idx1]
                idx1 -= 1
            rIdx -= 1

        while 0 <= idx2:
            nums1[rIdx] = nums2[idx2]
            idx2 -= 1
            rIdx -= 1

        while 0 <= idx1:
            nums1[rIdx] = nums1[idx1]
            idx1 -= 1
            rIdx -= 1

        return nums1[:m + n]


data = [([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1, 2, 0, 0, 0, 0], 2, [2, 5, 6], 3, [1, 2, 2, 5, 6]),
        ([1, 2, 3, 0, 0, 0], 3, [2, 6], 2, [1, 2, 2, 3, 6]),
        ([0], 0, [1], 1, [1])
       ]
s = Solution()
for nums1, m, nums2, n, expected in data:
    real = s.merge(nums1, m, nums2, n)
    print('{} {} / {} {}, expected {}, real {}, result {}'.format(nums1, m, nums2, n, expected, real, expected == real))
