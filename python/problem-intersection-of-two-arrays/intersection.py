#   https://leetcode.com/problems/intersection-of-two-arrays
#   71.76%


class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1).intersection(set(nums2)))


s = Solution()
print(s.intersection([1, 2, 2, 1], [2, 2]))
print(s.intersection([], [2, 2]))
