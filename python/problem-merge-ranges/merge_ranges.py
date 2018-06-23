# https://www.interviewcake.com/question/python/merging-ranges


def merge_ranges(arr):
  arr = sorted(arr, key=lambda t: t[0])
  result = []
  prev_s, prev_e = arr[0]
  for i, (cur_s, cur_e) in enumerate(arr):
    if i == 0:
      continue
    if prev_e < cur_s:
      result.append((prev_s, prev_e))
      prev_s, prev_e = cur_s, cur_e
    else:
      if prev_e <= cur_e:
        prev_e = cur_e
  result.append((prev_s, prev_e))
  return result


print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
print(merge_ranges([(0, 1), (3, 5), (4, 8), (5, 9), (10, 12), (9, 10)]))
print(merge_ranges([(1, 2), (2, 3)]))
print(merge_ranges([(1, 5), (2, 3)]))
print(merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9)]))
