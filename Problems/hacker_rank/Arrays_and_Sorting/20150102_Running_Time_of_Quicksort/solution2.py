def insertion_sort(arr):
  cnt = 0
  for i in range(1, len(arr)):
    for j in range(i, 0, -1):
      if arr[j] < arr[j - 1]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        cnt += 1
  return cnt

def quick_sort(ar):
  cnt, data = 0, []
  data.append((0, len(ar) - 1))
  while 0 < len(data):
    s, e = data.pop(0)
    if s >= e:
      continue
    i, j = s, s
    while i < e:
      if ar[i] < ar[e]:
        ar[i], ar[j] = ar[j], ar[i]
        i, j, cnt = i + 1, j + 1, cnt + 1
      else:
        i += 1
    ar[j], ar[e] = ar[e], ar[j]
    cnt += 1
    data.insert(0, (j + 1, e))
    data.insert(0, (s, j - 1))
  return cnt
  
if __name__ == '__main__':
  n = int(raw_input())
  ar = map(int, raw_input().split())
  print insertion_sort(list(ar)) - quick_sort(list(ar))
