#   https://leetcode.com/problems/remove-element


class Solution:
    #   96.38%
    def removeElement0(self, nums, val):
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

    #   82.26%
    def removeElement1(self, nums, val):
        if nums is None or 0 == len(nums):
            return 0
        lenNums = len(nums)
        l, r = 0, lenNums - 1
        while l < lenNums and val != nums[l]:
            l += 1
        while 0 <= r and val == nums[r]:
            r -= 1
        if r < l:
            return l
        print('before start\tl {} r {} nums {}'.format(l, r, nums))
        while l < r:
            while l < lenNums and val != nums[l]:
                l += 1
                print('l {}'.format(l))
            while 0 < r and val == nums[r]:
                r -= 1
                print('r {}'.format(r))
            if l < lenNums and 0 <= r and l < r:
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            print('l {} r {} nums {}'.format(l, r, nums))
        print('final\tl {} r {} nums {}'.format(l, r, nums))
        removeIdx = lenNums - 1
        while val == nums[removeIdx]:
            removeIdx -= 1
        return removeIdx + 1

    #   https://leetcode.com/problems/remove-element/solution
    def removeElement(self, nums, val):
        if nums is None or 0 == len(nums):
            return 0
        i = 0
        for j in range(len(nums)):
            if val != nums[j]:
                nums[i] = nums[j]
                i += 1
        return i


s = Solution()
data = [([3, 2, 2, 3], 3, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4]),
        ([3, 3], 3, []),
        ([3, 3], 5, [3, 3]),
        ([1, 2, 3, 4], 1, [4, 2, 3]),
        ]
for nums, val, expected in data:
    print(nums)
    real = s.removeElement(nums, val)
    print('{}, val {}, expected {}, real {}, result {}'.format(nums, val, expected, real, len(expected) == real))
