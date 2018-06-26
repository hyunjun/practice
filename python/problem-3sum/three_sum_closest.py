#   https://leetcode.com/problems/3sum-closest

#   https://leetcode.com/problems/3sum-closest/discuss/128797/Python44msbeats-100.00
#   https://leetcode.com/problems/3sum-closest/discuss/7963/PythonBeating-95-solution-with-two-pointersO(N-2)

import sys


class Solution:
    #   Time Limit Exceeded
    def threeSum0(self, nums, target):
        if nums is None or 0 == len(nums):
            return None

        nums.sort()
        lenNums = len(nums)

        twoSumDict = {}
        for i, n in enumerate(nums):
            for j in range(i + 1, lenNums):
                twoSumDict[(i, j)] = n + nums[j]

        twoSums = sorted(twoSumDict.items(), key=lambda t: t[1])
        lenTwoSums = len(twoSums)

        minDiff, result = sys.maxsize, sys.maxsize
        for i, n in enumerate(nums):
            for (j, k), twoSum in twoSums:
                if j <= i or k <= i:
                    continue
                threeSum = n + twoSum
                #print('{} + {} + {} = {}'.format(nums[i], nums[j], nums[k], threeSum))
                if abs(threeSum - target) < minDiff:
                    minDiff = abs(threeSum - target)
                    result = threeSum
                    #print('{} + {} + {} = {}, min diff {}, result {}'.format(nums[i], nums[j], nums[k], threeSum, minDiff, result))
                elif abs(threeSum - target) == minDiff:
                    minDiff = abs(threeSum - target)
                    result = min(result, threeSum)
        return result

    #   Wrong Answer
    def threeSum1(self, nums, target):
        if nums is None or 0 == len(nums):
            return None

        nums.sort()
        l, r, minDiff, result = 0, len(nums) - 1, sys.maxsize, sys.maxsize
        while 1 < r - l:
            curTarget = target - nums[l] - nums[r]
            ll, rr = l + 1, r - 1
            while ll <= rr:
                m = (ll + rr) // 2
                if curTarget == nums[m]:
                    return target
                curSum = nums[l] + nums[m] + nums[r]
                print('{} + {} + {} = {}'.format(nums[l], nums[m], nums[r], curSum))
                if abs(target - curSum) < minDiff:
                    minDiff = abs(target - curSum)
                    result = curSum
                print('nums[{}] = {} vs curSum {}'.format(m, nums[m], curSum))
                if nums[m] < curTarget:
                    ll = m + 1
                elif curTarget < nums[m]:
                    rr = m - 1
                else:
                    ll = m + 1
                    rr = m - 1
            if curSum < target:
                l += 1
            elif target < curSum:
                r -= 1
        return result

    #   2.52%
    def threeSum(self, nums, target):
        if nums is None or 0 == len(nums):
            return None

        nums.sort()
        lenNums = len(nums)
        twoSumDict = {}
        for i, n in enumerate(nums):
            for j in range(i + 1, lenNums):
                twoSumDict[(i, j)] = n + nums[j]
        twoSums = sorted(twoSumDict.items(), key=lambda t: t[1])
        lenTwoSums = len(twoSums)

        targetDict = {}
        for i, n in enumerate(nums):
            targetDict[i] = target - n

        #print(targetDict)
        #print(twoSums)
        minDiff, result = sys.maxsize, sys.maxsize
        for i, t in targetDict.items():
            l, r = 0, lenTwoSums - 1
            while l <= r:
                m = (l + r) // 2
                j, k = twoSums[m][0]
                curSum = nums[i] + nums[j] + nums[k]
                #print('{} + {} + {} = {}'.format(nums[i], nums[j], nums[k], curSum))
                if twoSums[m][1] == t:
                    if i != j and i != k:
                        return curSum
                    l = m + 1
                    r = m - 1
                elif twoSums[m][1] < t:
                    l = m + 1
                elif t < twoSums[m][1]:
                    r = m - 1
                if i != j and i != k:
                    curDiff = abs(target - curSum)
                    if curDiff < minDiff:
                        minDiff = curDiff
                        result = curSum
        return result


cases = [([1, 2, 4, 8, 16, 32, 64, 128], 82, 82), 
         ([-1, 2, 1, -4], 1, 2),
         ([-1, 2, 1, -4], 0, -1),
         ([-1, 2, 1, -4], -2, -3),
         ([-1, 2, 1, -4], -4, -4),
         ([-7, -71, -7, -13, 45, 46, -50, 83, -29, -72, 9, 32, -74, 81, 68, 92, -31, 28, -46, -86, -70, 31, -62, -20, -56, 97, -41, 21, 81, 17, -14, 56, 69, 16, 25, -38, 65, -48, 15, 16, -25, 68, -41, 46, -56, -2, -3, 82, 8, 19, -32, 62, 92, -56, -9, 43, 50, 100, 66, -45, 41, -24, -4, 83, -36, 79, 24, 97, 82, 89, -56, -91, 75, -64, -68, 96, -55, -52, -58, -37, 68, 27, 89, -40, -42, 94, -92, -70, 40, 74, 75, -15, 54, -54, 0, 4, -39, 93, 88, -31, -26, 93, 8, -85, -62, 89, -93, 98, 4, -58, 8, 5, -93, 7, 30, -75, 63, 41, 62, -52, 49, 93, -11, 87, 7, 52, 5, -96, -56, 43, -41, -75, -16, 73, 6, 35, -32, 62, -50, -57, -25, 5, -32, 94, -70, 6, 19, -12, 63, -47, 76, -57, 41, -49, -33, -15, -81, 55, 88, 67, -51, 100, -19, -39, 62, 84, -100, 78, -24, 31, -32, -83, 33, -25, 86, 9, -30, -40, 52, 64, -30, -17, 19, -69, -89, -67, -79, -100, -53], 157, 157),
        ]
s = Solution()
for nums, target, expected in cases:
    real = s.threeSum(nums, target)
    print('nums {}\ttarget {}\texpected {}\treal {}\tresult {}'.format(nums, target, expected, real, expected == real))
