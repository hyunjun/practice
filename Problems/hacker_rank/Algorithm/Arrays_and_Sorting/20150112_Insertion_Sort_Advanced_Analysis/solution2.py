def insertion_sort(arr):
  cnt, total_len = 0, len(arr)
  for i in xrange(1, total_len):
    for j in xrange(i, 0, -1):
      if arr[j] < arr[j - 1]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        cnt += 1
  return cnt


def insertion_sort2(arr):
  cnt, indices, counts = 0, {}, [0] * 1000000
  for i, a in enumerate(arr):
    indices.setdefault(a, []).append(i)
    counts[a - 1] += 1
  #print indices, counts
  cur, lasts = 0, []
  for i, a in enumerate(counts):
    if 0 < a:
      for idx in indices[i + 1]:
        for l in lasts:
          if idx < l:
            idx += 1
        if cur < idx:
          cnt += idx - cur
          lasts.append(idx)
        cur += 1
  return cnt


def merge_sort(arr):
  def merge(arr):
    l = len(arr)
    if l < 2:
      return arr, 0
    m = l / 2
    left, l_cnt = merge(arr[:m])
    right, r_cnt = merge(arr[m:])
    res = []
    cnt = l_cnt + r_cnt
    while 0 < len(left) and 0 < len(right):
      if left[0] <= right[0]:
        res.append(left.pop(0))
      else:
        cnt += len(left)
        print "\t{}".format(cnt),
        res.append(right.pop(0))
    print
    #print res, cnt
    res.extend(left)
    res.extend(right)
    return res, cnt
  return merge(arr)[1]

if __name__ == '__main__':
  for i in range(int(raw_input())):
    n = int(raw_input())
    arr = [int(i) for i in raw_input().split()]
    #print insertion_sort(arr)
    #print insertion_sort2(arr)
    print merge_sort(arr)
