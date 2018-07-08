#   https://leetcode.com/problems/next-greater-element-i
#   100.00%


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        if nums1 is None or 0 == len(nums1) or nums2 is None or 0 == len(nums2):
            return []
        idxDict = {}
        for i, n in enumerate(nums2):
            idxDict[n] = i
        res, lenNums2 = [], len(nums2)
        for n in nums1:
            idx = idxDict[n]
            while idx < lenNums2 and nums2[idx] <= n:
                idx += 1
            if idx == lenNums2:
                res.append(-1)
            else:
                res.append(nums2[idx])
        return res


s = Solution()
data = [([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
        ([2, 4], [1, 2, 3, 4], [3, -1]),
        ]
for nums1, nums2, expected in data:
    real = s.nextGreaterElement(nums1, nums2)
    print('{}, {}, expected {}, real {}, result {}'.format(nums1, nums2, expected, real, expected == real))
