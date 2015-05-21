from collections import Counter

if __name__ == '__main__':
  N = int(raw_input())
  A = [int(i) for i in raw_input().split()]
  M = int(raw_input())
  B = [int(i) for i in raw_input().split()]
  res, b_cnt_dict = [], Counter(B)
  for n, cnt in Counter(A).items():
    if cnt != b_cnt_dict[n]:
      res.append(n)
  print ' '.join([str(i) for i in sorted(res)])
