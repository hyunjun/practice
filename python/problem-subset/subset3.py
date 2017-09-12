# https://leetcode.com/problems/subsets
# 34.60%  recursive가 time limit에 걸려 다시 이 방식 사용
import math

class Solution(object):

  def subsets(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if nums is None or 0 == len(nums):
      return [[]]
    result = []
    for i in range(int(math.pow(2, len(nums)))):
      #print(i)
      idx, b = 0, i
      temp = []
      while 0 < b:
        if b & 0x1:
          #print('[{}] 1'.format(idx))
          temp.append(nums[idx])
        #else:
        #    print('[{}] 0'.format(idx))
        b >>= 1
        idx += 1
      result.append(temp)

    return result


s = Solution()
print(s.subsets([]))
print(s.subsets([1]))
print(s.subsets([1, 2]))
print(s.subsets([1, 2, 3]))
print(s.subsets([1,2,3,4,5,6,7,8,10,0]))
