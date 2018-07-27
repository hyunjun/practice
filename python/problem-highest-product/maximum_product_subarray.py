#   https://leetcode.com/problems/maximum-product-subarray

#   https://leetcode.com/problems/maximum-product-subarray/discuss/153372/Python-concise-O(n)-solution


import sys


class Solution:
    #   99.06%
    def maxProduct(self, nums):
        if 1 == len(nums):
            return nums[0]
        zeroIndices = [i for i, n in enumerate(nums) if 0 == n]

        def getNegNumsAndSEIndices(arr):
            start, end, count = -1, -1, 0
            for i, a in enumerate(arr):
                if a < 0:
                    if -1 == start:
                        start = i
                    end = i
                    count += 1
            return count, start, end

        def product(arr):
            if 0 == len(arr):
                return None
            p = arr[0]
            for i in range(1, len(arr)):
                p *= arr[i]
            return p

        def getProduct(arr):
            if 1 == len(arr):
                return arr[0]
            count, start, end = getNegNumsAndSEIndices(arr)
            if 0 == count or 0 == count % 2:
                return product(arr)
            l, r = product(arr[:end]), product(arr[start + 1:])
            if l is None:
                return r
            if r is None:
                return l
            return max(l, r)

        if 0 == len(zeroIndices):
            return getProduct(nums)
        maxVal, prevIdx = 0, 0
        zeroIndices.append(len(nums))
        for zIdx in zeroIndices:
            tmp = getProduct(nums[prevIdx:zIdx])
            if tmp is not None:
                maxVal = max(maxVal, tmp)
            prevIdx = zIdx + 1
        return maxVal


s = Solution()
data = [([2, 3, -2, 4], 6),
        ([2, 3, -2, -4], 48),
        ([2, 3, -2, -4, 5, -6], 240),
        ([-2, 0, -1], 0),
        ([-2], -2),
        ([-2, -3], 6),
        ([-2, 1], 1),
        ([0], 0),
        ([0, 2], 2),
        ]
for nums, expected in data:
    real = s.maxProduct(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
