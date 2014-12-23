def hasSubset(arr):
  i, max_num, no_set = 2, max(arr), set([0])
  while i < max_num + 1:
    print '[', i, ']', set([a % i for a in arr])
    if set([a % i for a in arr]) == no_set:
      return "NO"
    i += 1
  return "YES"


if __name__ == '__main__':
  T = int(raw_input())
  for i in range(T):
    N = int(raw_input())
    arr = map(int, raw_input().split())
    print hasSubset(arr)
