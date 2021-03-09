def print_ar(ar):
  print " ".join([str(a) for a in ar])


def partition(ar, l, r):
  pivot_item = ar[l]
  left = l
  right = r
  while left < right:
    while ar[left] <= pivot_item:
      left += 1
    while ar[right] > pivot_item:
      right -= 1
    if left < right:
      ar[left], ar[right] = ar[right], ar[left]
    ar[l] = ar[right]
    ar[right] = pivot_item
  return right

def quick_sort(ar):
  data = []
  data.append((ar, 0, len(ar) - 1))
  while 0 < len(data):
    arr, l, r = data.pop(0)
    arr, m = partition(arr, l, r)
    print_ar(arr)
    if l < m - 1:
      data.append((ar, l, m - 1))
    if m + 1 < r:
      data.append((ar, m + 1, r))

if __name__ == '__main__':
  n = int(raw_input())
  ar = map(int, raw_input().split())
  quick_sort(ar)
  # print partition([1, 2, 3, 5, 9, 7, 8], 4, 6)
