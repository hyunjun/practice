#   https://leetcode.com/problems/find-pivot-index

#   https://leetcode.com/problems/find-pivot-index/solution


class Solution:
    #   Wrong Answer
    def pivotIndex0(self, nums):
        if nums is None or 0 == len(nums):
            return -1
        l, r = 0, len(nums) - 1
        lSum, rSum = nums[l], nums[r]
        while l < r:
            if lSum < rSum:
                l += 1
                lSum += nums[l]
            elif lSum > rSum:
                r -= 1
                rSum += nums[r]
            else:
                if l + 1 == r - 1:
                    return l + 1
                l += 1
                r -= 1
                lSum += nums[l]
                rSum += nums[r]
        return -1

    #   0.0%
    def pivotIndex(self, nums):
        if nums is None or 0 == len(nums):
            return -1
        lSums = [nums[0]]
        for i in range(1, len(nums)):
            lSums.append(nums[i] + lSums[i - 1])
        rSums = [nums[len(nums) - 1]]
        for i in range(len(nums) - 2, -1, -1):
            rSums.insert(0, nums[i] + rSums[0])
        for i in range(len(nums)):
            if lSums[i] == rSums[i]:
                return i
        return -1


s = Solution()
data = [([1, 7, 3, 6, 5, 6], 3),
        ([1, 2, 3], -1),
        ([-1, -1, -1, -1, -1, -1], -1),
        ([-1, -1, -1, -1, -1, 0], 2),
        ]
for nums, expected in data:
    real = s.pivotIndex(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
