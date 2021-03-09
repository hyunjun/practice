def print_ar(ar):
  print " ".join([str(a) for a in ar])

def quick_sort(ar):
  data = []
  data.append((0, len(ar) - 2, len(ar) - 1))
  while 0 < len(data):
    s, e, p = data.pop(0)
    if s > e:
      continue
    #print 'target ar[{}:{}]'.format(s, e + 1), ar[s:e + 1], '\tpivot ar[{}] {}'.format(p, ar[p])
    b = []
    for i in range(s, e + 1):
      if ar[i] < ar[p]:
        if 0 < len(b):
          b_idx = b.pop(0)
          ar[b_idx], ar[i] = ar[i], ar[b_idx]
          if ar[p] < ar[i]:
            b.append(i)
      elif ar[p] < ar[i]:
        b.append(i)
    if 0 < len(b):
      b_idx = b.pop(0)
      if ar[p] < ar[b_idx]:
        ar[b_idx], ar[p] = ar[p], ar[b_idx]
        p = b_idx
    #print ar, (s, p - 2, p - 1), (p + 1, e, e + 1)
    print_ar(ar)
    data.append((s, p - 2, p - 1))
    data.append((p + 1, e, e + 1))

if __name__ == '__main__':
  n = int(raw_input())
  ar = map(int, raw_input().split())
  quick_sort(ar)
