#   https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

#   https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution


class Solution:
    #   95.53%
    def searchRange0(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                l = r = m
                while 0 <= l and nums[l] == target:
                    l -= 1
                while r < len(nums) and target == nums[r]:
                    r += 1
                return [l + 1, r - 1]
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return [-1, -1]

    #   1.16%
    def searchRange(self, nums, target):
        def lower(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if (0 <= m - 1 and nums[m - 1] < target <= nums[m]) or (0 == m and target == nums[m]):
                    if target == nums[m]:
                        return m
                if 0 <= m - 1 and target <= nums[m - 1]:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    break
            return -1

        def upper(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if (m == len(nums) - 1 and nums[m] == target) or (m + 1 < len(nums) and nums[m] <= target < nums[m + 1]):
                    if nums[m] == target:
                        return m
                if target < nums[m]:
                    r = m - 1
                elif m + 1 < len(nums) and nums[m + 1] <= target:
                    l = m + 1
                else:
                    break
            return -1

        return [lower(nums, target), upper(nums, target)]


s = Solution()
data = [([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 4, [-1, -1]),
        ([5, 7, 7, 8, 8, 10], 5, [0, 0]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([5, 7, 7, 8, 8, 10], 9, [-1, -1]),
        ([5, 7, 7, 8, 8, 10], 10, [5, 5]),
        ([5, 7, 7, 8, 8, 10], 11, [-1, -1]),
        ]
for nums, target, expected in data:
    real = s.searchRange(nums, target)
    print('{}, {}, expected {}, real {}, result {}'.format(nums, target, expected, real, expected == real))
