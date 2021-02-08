# https://www.youtube.com/watch?v=nqlNzOcnCfs


class Solution:
  def __init__(self):
    self.result = []

  def recur(self, acc, rest, target):
    if sum(acc) == target:
      self.result.append(acc[:])
    for i, r in enumerate(rest):
      acc.append(r)
      self.recur(acc, rest[i + 1:], target)
      acc.pop()

  def addUpToRecur(self, nums, target):
    if nums is None or 0 == len(nums):
      return []

    nums.sort(reverse=True)
    self.recur([], nums, target)
    return self.result

  def dp(self, arr, total, i, mem):
    key = str(total) + ':' + str(i)
    if key in mem:
      return mem[key]
    if 0 == total:
      return 1
    elif total < 0:
      return 0
    elif i < 0:
      return 0
    elif total < arr[i]:
      ret = self.dp(arr, total, i - 1, mem)
    else:
      ret = self.dp(arr, total - arr[i], i - 1, mem) + self.dp(arr, total, i - 1, mem)
    mem[key] = ret
    return ret

  def count_sets_dp(self, arr, total):
    mem = {}
    return self.dp(arr, total, len(arr) - 1, mem)


nums = [2, 4, 6, 10]
target = 16


s = Solution()
print(s.addUpToRecur(nums, target), s.count_sets_dp(nums, target))
