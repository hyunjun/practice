#   https://leetcode.com/problems/remove-element
#   96.38%


class Solution:
    def removeElement(self, nums, val):
        if nums is None or 0 == len(nums):
            return 0
        idx, removeIdx = 0, 0
        while removeIdx < len(nums):
            if val == nums[removeIdx]:
                idx = removeIdx
                while idx < len(nums) and val == nums[idx]:
                    idx += 1
                if idx < len(nums):
                    nums[removeIdx], nums[idx] = nums[idx], nums[removeIdx]
            removeIdx += 1
        for i in range(len(nums)):
            if nums[i] == val:
                removeIdx = i
                break
        print(idx, removeIdx)
        return removeIdx


s = Solution()
data = [([3, 2, 2, 3], 3, [2, 2]), ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4])]
for nums, val, expected in data:
    print(nums)
    real = s.removeElement(nums, val)
    print('{}, val {}, expected {}, real {}, result {}'.format(nums, val, expected, real, len(expected) == real))
