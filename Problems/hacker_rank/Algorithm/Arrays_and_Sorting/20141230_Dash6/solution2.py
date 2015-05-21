def partition(ar):
  return [a for a in ar if a < ar[0]] + ar[:1] + [a for a in ar if ar[0] < a]

  
if __name__ == '__main__':
  n = int(raw_input())
  ar = map(int, raw_input().split())
  res = partition(ar)
  print " ".join([str(r) for r in res])
