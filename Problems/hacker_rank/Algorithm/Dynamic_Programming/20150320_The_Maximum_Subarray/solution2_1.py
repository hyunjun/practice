def sum_of_maximum_subarray(arr):
  if 0 == len(arr):
    return '0 0'
  max_acc = cur_acc = arr[0]
  for a in arr[1:]:
    if cur_acc < 0:
      cur_acc = a
    else:
      cur_acc += a
    if max_acc < cur_acc:
      max_acc = cur_acc
  positive_arr = [a for a in arr if 0 < a]
  if len(positive_arr) == 0:
    non_cont_max = max(arr)
  else:
    non_cont_max = sum(positive_arr)
  return '%d %d' % (max_acc, non_cont_max)

if __name__ == '__main__':
  T = int(raw_input())
  for i in range(T):
    N = int(raw_input())
    arr = [int(n) for n in raw_input().split()]
    print sum_of_maximum_subarray(arr)
