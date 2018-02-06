# https://leetcode.com/problems/permutations-ii/description/
# 29.34%
# 전체 permutation을 모두 만들고 중복을 제거하면 느림
# unique한 number를 node value로 갖는 tree를 만들어
# root부터 leaf까지 value들을 하나의 permutation으로 생각하면 됨
# 예를 들어 1, 2, 1이라면 다음과 같이 3개의 leaf를 갖는 tree가 됨
#    root
#    /  |
#   1   2
#  / |  |
# 1  2  1
# |  |  |
# 2  1  1

from collections import Counter


class Solution:
  def __init__(self):
    self.result = []

  def recur(self, countDict, perm):
    #print('recur {} perm {}'.format(countDict, perm))
    vals = set(countDict.values())
    if {0} == vals:
      #print(perm)
      self.result.append(perm[:])
    else:
      for k, v in countDict.copy().items():
        if 0 == v:
          continue
        #print('k {} v {}'.format(k, v))
        countDict[k] -= 1
        perm.append(k)
        #print('before call; recur {} perm {}'.format(countDict, perm))
        self.recur(countDict, perm)
        countDict[k] += 1
        perm.pop()
        #print(' after call; recur {} perm {}'.format(countDict, perm))

  def permuteUnique(self, nums):
    if nums is None or 0 == len(nums):
      return []
    if 1 == len(nums):
      return [nums]

    countDict = Counter(nums)
    print(countDict)
    self.recur(countDict, [])

    return self.result


s = Solution()
nums = [1, 2, 1]
nums = [1, 2, 1, 2]
nums = [0, 1, 1, 2, 0, 1, 2, 0]
print(s.permuteUnique(nums))
