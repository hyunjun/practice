# https://leetcode.com/problems/sort-colors/description/
# 84.01%

class Solution(object):
  def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if nums is None or 0 == len(nums):
      return None

    d = {0:0, 1:0, 2:0}
    for n in nums:
      d[n] += 1
    print(d)
    idx = 0
    for key in range(3):
      i = 0
      while i < d[key]:
        nums[idx] = key
        i += 1
        idx += 1
    print('nums {}'.format(nums))


s = Solution()
s.sortColors([0])
s.sortColors([1, 0])
s.sortColors([0, 0, 1, 1, 2, 1, 2, 0, 2])