#   https://leetcode.com/problems/non-decreasing-array

#   https://leetcode.com/problems/non-decreasing-array/solution


class Solution:
    #   Wrong Answer
    def checkPossibility0(self, nums):
        if nums is None or 0 == len(nums):
            return True
        decreasingCount = 0
        for i, n in enumerate(nums):
            if i == 0:
                continue
            if nums[i - 1] > n:
                decreasingCount += 1
                if 1 < decreasingCount:
                    return False
        return True

    #   Wrong Answer
    def checkPossibility1(self, nums):
        if nums is None or 0 == len(nums):
            return True
        curMinVal, increasingCount = nums[len(nums) - 1], 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= curMinVal:
                curMinVal = nums[i]
            else:
                increasingCount += 1
                if 1 < increasingCount:
                    return False
        return True

    #   Wrong Answer
    def checkPossibility2(self, nums):
        if nums is None or 0 == len(nums):
            return True
        max1, max2, decreasingCount = nums[0], None, 0
        for i, n in enumerate(nums):
            if i == 0:
                continue
            if max1 <= n:
                max2 = max1
                max1 = n
            elif max2 is None or max2 <= n:
                if max2 is None:
                    max2 = n
                else:
                    max2 = n
                    decreasingCount += 1
            else:
                if max2 < max1:
                    return False
                else:
                    decreasingCount += 1
            if 1 < decreasingCount:
                return False
        return True

    #   12.63%
    def checkPossibility(self, nums):
        if nums is None or 0 == len(nums):
            return True
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] > nums[i]:
                if i + 1 < len(nums) and nums[i - 1] > nums[i + 1]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                break
        for i, n in enumerate(nums):
            if 0 == i:
                continue
            if nums[i - 1] > n:
                return False
        return True


s = Solution()
data = [([4, 2, 3], True),
        ([4, 2, 1], False),
        ([4, 4, 4], True),
        ([1, 2, 3], True),
        ([3, 4, 2, 3], False),
        ([1, 5, 4, 6, 7, 10, 8, 9], False),
        ([2, 3, 3, 2, 4], True),
        ([2, 3, 3, 2, 3, 3, 2, 4], False),
        ([-1, 4, 2, 3], True),
        ([3, 3, 2, 2], False),
        ]
for nums, expected in data:
    real = s.checkPossibility(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
