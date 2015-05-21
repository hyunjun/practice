def insertion_sort(arr):
  cnt = 0
  for i in range(1, len(arr)):
    for j in range(i, 0, -1):
      if arr[j] < arr[j - 1]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        cnt += 1
  return cnt


if __name__ == '__main__':
  s = int(input())
  arr = list(map(int, input().split()))
  print(insertion_sort(arr))
