#   https://leetcode.com/problems/search-in-rotated-sorted-array-ii

#   https://leetcode.com/problems/search-in-rotated-sorted-array-ii/solution


from typing import List


class Solution:
    #   https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3537
    #   runtime; 56ms, 24.98%
    #   memory; 14.9MB
    def search(self, nums: List[int], target: int) -> bool:
        if nums is None or 0 == len(nums):
            return False

        def binarySearch(arr):
            print(arr)
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if arr[m] == target:
                    return True
                if target < arr[m]:
                    r = m - 1
                else:
                    l = m + 1
            return False

        if nums[0] < nums[-1]:
            return binarySearch(nums)
        m = len(nums) // 2
        if nums[m] == target:
            return True
        return self.search(nums[:m], target) or self.search(nums[m + 1:], target)



s = Solution()
data = [([2,5,6,0,0,1,2], -1, False),
        ([2,5,6,0,0,1,2], 0, True),
        ([2,5,6,0,0,1,2], 1, True),
        ([2,5,6,0,0,1,2], 2, True),
        ([2,5,6,0,0,1,2], 3, False),
        ([2,5,6,0,0,1,2], 4, False),
        ([2,5,6,0,0,1,2], 5, True),
        ([2,5,6,0,0,1,2], 6, True),
        ([2,5,6,0,0,1,2], 7, False),
        ]
for nums, target, expect in data:
    real = s.search(nums, target)
    print(f'{nums} {target} expect {expect} real {real} result {expect == real}')
