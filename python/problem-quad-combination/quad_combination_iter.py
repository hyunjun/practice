# https://www.pramp.com/question/gKQ5zA52mySBOA5GALj9


def quad_combination(s, arr):
  sorted_arr = sorted(inp)

  d, arr_len = {}, len(arr)
  for i in range(0, arr_len):
    for j in range(i + 1, arr_len):
      sub_sum = sorted_arr[i] + sorted_arr[j]
      if sub_sum < s:
        d[(i, j)] = sub_sum

  result = set()
  for (i, j), v1 in d.items():
    for (k, l), v2 in d.items():
      if i >= k or j >= l or i >= l or j >= k or v1 + v2 != s:
        continue
      result.add((sorted_arr[i], sorted_arr[j], sorted_arr[k], sorted_arr[l]))

  print result


inp, s = [0, 7, 5, 1, 8, 9, 2, 3], 17
print quad_combination(s, inp)
