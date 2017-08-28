# https://leetcode.com/problems/move-zeroes
# 7.54%

class Solution(object):
  def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if nums is None or 0 == len(nums):
      return

    l = len(nums)

    zeroIdx = 0
    while zeroIdx < l and nums[zeroIdx] != 0:
      zeroIdx += 1
    nonZeroIdx = zeroIdx + 1
    while nonZeroIdx < l and nums[nonZeroIdx] == 0:
      nonZeroIdx += 1
    print('zero idx {}\tnon zero idx {}'.format(zeroIdx, nonZeroIdx))
    while zeroIdx < l and nonZeroIdx < l:
      nums[zeroIdx], nums[nonZeroIdx] = nums[nonZeroIdx], nums[zeroIdx]
      while nums[zeroIdx] != 0:
        zeroIdx += 1
      nonZeroIdx = zeroIdx + 1
      while nonZeroIdx < l and nums[nonZeroIdx] == 0:
        nonZeroIdx += 1
      print('zero idx {}\tnon zero idx {}\t{}'.format(zeroIdx, nonZeroIdx, nums))

nums = [0, 1, 0, 3, 12] # [1, 3, 12, 0, 0]
nums = [0]
s = Solution()
s.moveZeroes(nums)
print(nums)
