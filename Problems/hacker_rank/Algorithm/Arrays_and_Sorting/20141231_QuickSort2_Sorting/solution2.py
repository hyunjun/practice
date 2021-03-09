def print_ar(ar):
  print " ".join([str(a) for a in ar])

def partition(ar):
  left = [a for a in ar if a < ar[0]]
  if 1 < len(left):
    left = partition([a for a in ar if a < ar[0]])
    print_ar(left)
  right = [a for a in ar if ar[0] < a]
  if 1 < len(right):
    right = partition([a for a in ar if ar[0] < a])
    print_ar(right)
  return left + ar[:1] + right


if __name__ == '__main__':
  n = int(raw_input())
  ar = map(int, raw_input().split())
  res = partition(ar)
  print_ar(res)
