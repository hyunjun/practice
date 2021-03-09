def print_ar(ar):
  print " ".join([str(a) for a in ar])

def quick_sort(ar):
  data = []
  data.append((0, len(ar) - 1))
  while 0 < len(data):
    s, e = data.pop(0)
    if s >= e:
      continue
    i, j = s, s
    while i < e:
      if ar[i] < ar[e]:
        ar[i], ar[j] = ar[j], ar[i]
        i, j = i + 1, j + 1
      else:
        i += 1
    ar[j], ar[e] = ar[e], ar[j]
    print_ar(ar)
    data.insert(0, (j + 1, e))
    data.insert(0, (s, j - 1))

if __name__ == '__main__':
  n = int(raw_input())
  ar = map(int, raw_input().split())
  quick_sort(ar)
