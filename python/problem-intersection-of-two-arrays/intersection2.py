#   https://leetcode.com/problems/intersection-of-two-arrays-ii/
#   46.15%


from collections import Counter


class Solution:
    def intersect(self, nums1, nums2):
        countDict1 = Counter(nums1)
        countDict2 = Counter(nums2)
        intersectionSet = set(nums1).intersection(set(nums2))
        result = []
        for i in intersectionSet:
            result.extend([i] * min(countDict1[i], countDict2[i]))
        return result


s = Solution()
print(s.intersect([1, 2, 2, 1], [2, 2]))
print(s.intersect([], [2, 2]))
