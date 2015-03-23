def sum_of_maximum_subarray(arr):
  if 0 == len(arr):
    return '0 0'
  non_contiguous = sum([a for a in arr if 0 < a])
  acc_sum = max_sum = arr[0]
  for a in arr[1:]:
    acc_sum += a
    if max_sum < acc_sum:
      if acc_sum < a:
        max_sum = a
      else:
        max_sum = acc_sum
  if max_sum < 0:
    non_contiguous = max_sum
  return '{} {}'.format(max_sum, non_contiguous)

if __name__ == '__main__':
  T = int(raw_input())
  for i in range(T):
    N = int(raw_input())
    arr = [int(n) for n in raw_input().split()]
    print sum_of_maximum_subarray(arr)
