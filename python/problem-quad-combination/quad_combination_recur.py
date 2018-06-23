# https://www.pramp.com/question/gKQ5zA52mySBOA5GALj9


def quad_combination(s, acc, arr):
  if 4 == len(acc):
    if s == sum(acc):
      return [acc[:]] # return list of copy of acc, NOT list of acc
    else:
      return None
  else:
    tmp = []
    for i in range(0, len(arr)):
      acc.append(arr[i])
      if 0 <= s - sum(acc) <= sum(arr[i + 1:]):
        tmp.extend(quad_combination(s, acc, arr[i + 1:]))
      acc.pop()
    return tmp


inp, s = [0, 7, 5, 1, 8, 9, 2, 3], 17
sorted_inp = sorted(inp, reverse=True)
print(quad_combination(s, [], sorted_inp))
