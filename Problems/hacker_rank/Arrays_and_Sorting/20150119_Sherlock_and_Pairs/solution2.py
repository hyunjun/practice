def num_of_pairs(ar):
  cnt_dict, cnt = {}, 0
  [cnt_dict.setdefault(a, []).append(1) for a in ar]
  for k, v in cnt_dict.items():
    l = len(v)
    if 1 < l:
      cnt += l * (l - 1)
  return cnt


if __name__ == '__main__':
  for i in range(int(raw_input())):
    raw_input()
    print num_of_pairs([int(i) for i in raw_input().split()])
