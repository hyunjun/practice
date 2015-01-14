def print_ar(ar):
  print " ".join([str(a) for a in ar])

def partition(ar, s, e):
  i, j = s, s
  while i < e:
    if ar[i] < ar[e]:
      ar[i], ar[j] = ar[j], ar[i]
      i, j = i + 1, j + 1
    else:
      i += 1
  ar[j], ar[e] = ar[e], ar[j]
  print_ar(ar)
  return j

def quick_sort(ar, s, e):
  if s >= e:
    return
  p = partition(ar, s, e)
  quick_sort(ar, s, p - 1)
  quick_sort(ar, p + 1, e)
  
if __name__ == '__main__':
  n = int(raw_input())
  ar = map(int, raw_input().split())
  quick_sort(ar, 0, len(ar) - 1)
