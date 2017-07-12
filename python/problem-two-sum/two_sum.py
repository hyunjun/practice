# https://leetcode.com/problems/two-sum

def indices_of_two(arr, target):
  idx_dict = {}
  for i, n in enumerate(arr):
    m = target - n
    if m in idx_dict:
      return [idx_dict[m], i]
    idx_dict[n] = i
  return [None, None]


for arr, target in [([2, 7, 11, 15], 9), ([3, 3], 6), ([3, 2, 4], 6), ([-3, 4, 3, 90], 0)]:
  print(arr, target, indices_of_two(arr, target))