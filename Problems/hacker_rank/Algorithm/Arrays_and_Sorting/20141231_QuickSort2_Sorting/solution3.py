def print_ar(ar):
  print(" ".join([str(a) for a in ar]))

def quick_sort(ar):
  left = [a for a in ar if a < ar[0]]
  if 1 < len(left):
    left = quick_sort([a for a in ar if a < ar[0]])
    print_ar(left)
  right = [a for a in ar if ar[0] < a]
  if 1 < len(right):
    right = quick_sort([a for a in ar if ar[0] < a])
    print_ar(right)
  return left + ar[:1] + right


if __name__ == '__main__':
  n = int(input())
  ar = list(map(int, input().split()))
  res = quick_sort(ar)
  print_ar(res)
