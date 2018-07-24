#   https://leetcode.com/problems/shortest-unsorted-continuous-subarray

#   https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solution


class Solution:
    #   Wrong Answer
    def findUnsortedSubarray0(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        s, e = None, None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                j = i
                while 0 < j and nums[j - 1] == nums[j]:
                    j -= 1
                s = j
                break
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] > nums[i]:
                j = i
                while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    j += 1
                e = j
                break
        if s is None and e is None:
            return 0
        return e - s + 1

    #   Wrong Answer
    def findUnsortedSubarray1(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        l, r = 0, len(nums) - 1
        while l < len(nums) - 1 and nums[l] < nums[r] and nums[l] < nums[l + 1]:
            l += 1
        while 0 < r and nums[l] <= nums[r] and nums[r - 1] <= nums[r]:
            r -= 1
        if l >= r or nums[l] == nums[r]:
            return 0
        return r - l + 1

    #   55.84%
    def findUnsortedSubarray(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        sortedNums = sorted(nums)
        l, r = 0, len(nums) - 1
        while l < len(nums) - 1 and nums[l] == sortedNums[l]:
            l += 1
        while 0 < r and nums[r] == sortedNums[r]:
            r -= 1
        if l >= r:
            return 0
        return r - l + 1


s = Solution()
data = [([2, 6, 4, 8, 10, 9, 15], 5),
        ([1, 2, 3, 4, 5], 0),
        ([1, 2, 4, 3, 4], 2),
        ([4, 3, 2, 1, 0], 5),
        ([1, 1, 1], 0),
        ([1, 3, 2, 2, 2], 4),
        ([1, 1, 3, 3, 2, 2, 2], 5),
        ([1, 2, 4, 5, 3], 3),
        ([2, 3, 3, 2, 4], 3),
        ([1, 3, 4, 2, 5], 3),
        ]
for nums, expected in data:
    real = s.findUnsortedSubarray(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
