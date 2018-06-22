# https://leetcode.com/problems/move-zeroes

# https://leetcode.com/problems/move-zeroes/solution


class Solution(object):
  # 7.54%
  def moveZeroes0(self, nums):
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

  # 31.68%
  def moveZeroes1(self, nums):
    if nums is None or 0 == len(nums):
      return

    dst = 0
    for src in range(len(nums)):
      if 0 != nums[src]:
        nums[dst] = nums[src]
        dst += 1
    for i in range(dst, len(nums)):
      nums[i] = 0

  # 32.31%
  def moveZeroes(self, nums):
    if nums is None or 0 == len(nums):
      return

    dst = 0
    for src in range(len(nums)):
      if 0 != nums[src]:
        nums[dst], nums[src] = nums[src], nums[dst]
        dst += 1


nums = [0, 1, 0, 3, 12] # [1, 3, 12, 0, 0]
nums = [0]
s = Solution()
s.moveZeroes(nums)
print(nums)
