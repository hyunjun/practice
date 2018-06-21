#   https://leetcode.com/problems/median-of-two-sorted-arrays
#   77.02%

#   https://leetcode.com/problems/median-of-two-sorted-arrays/solution
#   https://fizzbuzzed.com/top-interview-questions-2


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if (nums1 is None or 0 == len(nums1)) and (nums2 is None or 0 == len(nums2)):
            return 0
        len1, len2 = len(nums1), len(nums2)
        idx1, idx2 = 0, 0
        sortedIdx, maxSortedIdx = 0, (len1 + len2) // 2
        sortedNums = [None] * (maxSortedIdx + 1)
        while sortedIdx <= maxSortedIdx:
            if idx1 < len1 and idx2 < len2:
                if nums1[idx1] <= nums2[idx2]:
                    sortedNums[sortedIdx] = nums1[idx1]
                    idx1 += 1
                else:
                    sortedNums[sortedIdx] = nums2[idx2]
                    idx2 += 1
            elif idx2 == len2:
                sortedNums[sortedIdx] = nums1[idx1]
                idx1 += 1
            elif idx1 == len1:
                sortedNums[sortedIdx] = nums2[idx2]
                idx2 += 1
            #print(sortedIdx, sortedNums, nums1, idx1, nums2, idx2)
            sortedIdx += 1
        if 0 == (len1 + len2) % 2:
            #print(maxSortedIdx, sortedNums, sum(sortedNums[-2:]) / 2)
            return sum(sortedNums[-2:]) / 2
        #print(maxSortedIdx, sortedNums, sortedNums[-1])
        return sortedNums[-1]


s = Solution()
data = [([1], [1], 1.0),
        ([100001], [100000], 100000.5),
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([1, 2, 3], [4, 5, 6], 3.5),
        ([1, 3, 5], [2, 4], 3),
        ([1, 3, 5], [2, 4, 6], 3.5),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], [10], 5.5),
        ]
for nums1, nums2, median in data:
    real = s.findMedianSortedArrays(nums1, nums2)
    print('{}, {}, expected {}, real {}, result {}'.format(nums1, nums2, median, real, median == real))
