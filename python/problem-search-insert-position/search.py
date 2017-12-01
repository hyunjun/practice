#   https://leetcode.com/problems/search-insert-position
#   47.19%
#   one liner
#   return len([x for x in nums if x<target])

class Solution:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1

        if target <= nums[l]:
            return l
        if nums[r] < target:
            return r + 1

        #for i, num in enumerate(nums):
        #    if target <= num:
        #        return i
        while l < r:
            m = ((l + r) // 2)
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m - 1
                if nums[r] < target:
                    return m
            else:   #   nums[m] < target
                l = m + 1
                if target <= nums[l]:
                    return l
        return -1


s = Solution()
nums = [1, 3, 5, 7]
cases = [(0, 0), (1, 0), (2, 1), (3, 1), (4, 2), (5, 2), (6, 3), (7, 3), (8, 4)]
for target, expected in cases:
    real = s.searchInsert(nums, target)
    print('{}\ttarget {}\texpected {}\treal {}\tresult {}'.format(nums, target, expected, real, expected == real))
