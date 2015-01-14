def merge_sort(arr):
  def merge(arr):
    l = len(arr)
    if l < 2:
      return arr, 0
    m = int(l / 2)
    left, l_cnt = merge(arr[:m])
    right, r_cnt = merge(arr[m:])
    res = []
    cnt = l_cnt + r_cnt
    while 0 < len(left) and 0 < len(right):
      if left[0] <= right[0]:
        res.append(left.pop(0))
      else:
        cnt += len(left)
        res.append(right.pop(0))
    res.extend(left)
    res.extend(right)
    return res, cnt
  return merge(arr)[1]

if __name__ == '__main__':
  for i in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(merge_sort(arr))
