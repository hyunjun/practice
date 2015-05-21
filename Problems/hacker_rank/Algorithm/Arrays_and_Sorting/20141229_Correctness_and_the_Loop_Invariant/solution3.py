def insertion_sort(arr):
  for i in range(1, len(arr)):
    for j in range(i, 0, -1):
      if arr[j] < arr[j - 1]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
  print(' '.join([str(a) for a in arr]))


if __name__ == '__main__':
  s = int(input())
  arr = list(map(int, input().split()))
  insertion_sort(arr)
