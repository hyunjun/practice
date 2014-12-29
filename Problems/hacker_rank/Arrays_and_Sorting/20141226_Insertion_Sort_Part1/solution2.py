def insertion_sort(arr):
  V, idx = arr[-1], len(arr) - 2
  while -1 < idx and V < arr[idx]:
    arr[idx + 1] = arr[idx]
    print ' '.join([str(a) for a in arr])
    idx -= 1
  arr[idx + 1] = V
  print ' '.join([str(a) for a in arr])


if __name__ == '__main__':
  s = int(raw_input())
  arr = map(int, raw_input().split())
  insertion_sort(arr)
