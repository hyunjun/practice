#   https://leetcode.com/problems/next-permutation

#   https://leetcode.com/problems/next-permutation/solution


class Solution:
    #   Wrong Answer
    def nextPermutation0(self, nums):
        sortedNums = sorted(nums)
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                j = len(nums) - 1
                while nums[i - 1] < sortedNums[j]:
                    j -= 1
                j += 1
                for k in range(i, len(nums)):
                    if nums[k] == sortedNums[j]:
                        break
                nums[i - 1], nums[i:] = nums[k], nums[i - 1:k] + nums[k + 1:]
                return
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    #   94.27%
    def nextPermutation(self, nums):
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                nextVal, sortedNums = None, sorted(nums[i:])
                for j in range(len(sortedNums)):
                    if nums[i - 1] < sortedNums[j]:
                        nextVal = sortedNums[j]
                        break
                k = i
                for j in range(i, len(nums)):
                    if nextVal == nums[j]:
                        k = j
                        break
                nums[i - 1], nums[i:] = nums[k], sorted(nums[i - 1:j] + nums[k + 1:])
                return
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1



s = Solution()
data = [([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 3, 2], [2, 1, 3]),
        ([2, 3, 1], [3, 1, 2]),
        ([1, 1, 5], [1, 5, 1]),
        ([1, 5, 1, 1], [5, 1, 1, 1]),
        ([2, 3, 0, 2, 4, 1], [2, 3, 0, 4, 1, 2]),
        ]
for nums, expected in data:
    print(nums)
    s.nextPermutation(nums)
    print('expected {}, real {}, result {}'.format(expected, nums, nums == expected))
