def extend_num(n, max_str_len):
  s = str(n)
  additional_num = s[0]
  # while len(s) < max_str_len:
  #   s += additional_num
  # return s
  return s + additional_num * (max_str_len - len(s))


def sort_list(l):
  max_str_len = max(map(lambda s: len(str(s)), l))
  l = [(x, int(str(x)[0]), int(extend_num(x, max_str_len))) for x in l]
  return sorted(l, key=lambda t: (t[1], t[2]), reverse=True)


def print_first_item(l):
  return ''.join([str(t[0]) for t in l])


ll = [[9, 50, 1, 2], [9, 5, 51, 50, 1, 2], [9, 500, 5, 51, 50, 1, 2], [56, 53, 50, 9, 1, 2, 5]]
for l in ll:
  print l, print_first_item(sort_list(l))
