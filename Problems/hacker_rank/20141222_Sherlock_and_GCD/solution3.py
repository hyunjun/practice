def hasSubset(arr):
  i, max_num, no_set = 2, max(arr), {0}
  while i < max_num + 1:
    if {a % i for a in arr} == no_set:
      return "NO"
    i += 1
  return "YES"


if __name__ == '__main__':
  T = int(input())
  for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(hasSubset(arr))
