# https://leetcode.com/problems/range-sum-query-mutable/
import math


class NumArray(object):
  def __init__(self, nums):
    """
    :type nums: List[int]
    """
    self.nums = nums
    self.len_nums = len(self.nums)
    #print('{}\t{}'.format(self.nums, self.len_nums))
    self.numInBlocks = math.floor(math.sqrt(self.len_nums))
    #print('num in blocks {}'.format(self.numInBlocks))
    numOfBlocks = self.len_nums // self.numInBlocks
    #print('num of blocks {}'.format(numOfBlocks))
    if numOfBlocks * self.numInBlocks < self.len_nums:
      numOfBlocks += 1
    self.blockedNums = [0] * (numOfBlocks)
    #print('blockedNums {}'.format(self.blockedNums))
    for i, n in enumerate(self.nums):
      blockNum = i // self.numInBlocks
      #print('block num {}'.format(blockNum))
      self.blockedNums[blockNum] += n


  def update(self, i, val):
    """
    :type i: int
    :type val: int
    :rtype: void
    """
    updated = val - self.nums[i]
    self.nums[i] = val
    self.blockedNums[i // self.numInBlocks] += updated

  def sumRange(self, i, j):
    """
    :type i: int
    :type j: int
    :rtype: int
    """
    if i == j:
      return self.nums[i]

    lBlockNum = i // self.numInBlocks
    rBlockNum = j // self.numInBlocks
    #print('l block num {}\tr block num {}'.format(lBlockNum, rBlockNum))

    result = 0
    if lBlockNum == rBlockNum:
      while i <= j:
        result += self.nums[i]
        i += 1
    else:
      lBlockNum += 1
      while i // self.numInBlocks < lBlockNum:
        #print('left\t{} < {}'.format(i // self.numInBlocks, lBlockNum))
        result += self.nums[i]
        i += 1
      while lBlockNum < rBlockNum:
        #print('block\t{} < {}'.format(lBlockNum, rBlockNum))
        result += self.blockedNums[lBlockNum]
        lBlockNum += 1
      rIdx = rBlockNum * self.numInBlocks
      while rIdx <= j:
        #print('right\t{} < {}'.format(rIdx, j))
        result += self.nums[rIdx]
        rIdx += 1
    return result



nums = [1, 3, 5]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
obj.update(1, 2)
print(obj.sumRange(0, 2))

nums = [1, 3, 11, 6, 7, 10, 14, 9, 18, 16, 5, 4, 2, 8, 19]
obj = NumArray(nums)
print(obj.sumRange(2, 10))

nums = [0, 9, 5, 7, 3]
obj = NumArray(nums)
for i, j in [[4,4],[2,4],[3,3]]:
  print('obj.sumRange({}, {}) = {}'.format(i, j, obj.sumRange(i, j)))
for i, val in [[4,5],[1,7],[0,8]]:
  obj.update(i, val)
print(obj.nums)
print('obj.sumRange({}, {}) = {}'.format(1, 2, obj.sumRange(1, 2)))
obj.update(1,9)
print(obj.nums)
print('obj.sumRange({}, {}) = {}'.format(4, 4, obj.sumRange(4, 4)))

#nums = []
#obj = NumArray(nums)

#[sumRange","sumRange","update","update","sumRange","sumRange","update","update"]
nums = [-28,-39,53,65,11,-56,-65,-39,-43,97]
obj = NumArray(nums)
print('obj.sumRange({}, {}) = {}'.format(5, 6, obj.sumRange(5, 6)))
obj.update(9,27)
print(obj.nums)
print('obj.sumRange({}, {}) = {}'.format(2, 3, obj.sumRange(2, 3)))
print('obj.sumRange({}, {}) = {}'.format(6, 7, obj.sumRange(6, 7)))
#[1,-82],[3,-72],[3,7],[1,8],[5,13],[4,-67]]