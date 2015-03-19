def has_same_sum_index(arr):
  if len(arr) == 1:
    return True
  if len(arr) == 2:
    return False
  l_sum, r_sum = sum(arr[:1]), sum(arr[2:])
  if l_sum == r_sum:
    return True
  for i in range(2, len(arr) - 1):
    l_sum += arr[i - 1]
    r_sum -= arr[i]
    if l_sum == r_sum:
      return True
  return False

if __name__ == '__main__':
  T = int(raw_input())
  for i in range(T):
    N = int(raw_input())
    arr = [int(n) for n in raw_input().split()]
    if has_same_sum_index(arr):
      print "YES"
    else:
      print "NO"
