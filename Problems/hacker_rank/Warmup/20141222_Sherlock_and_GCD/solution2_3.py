no_set = set([0])

def hasGCD(arr):
  max_num = max(arr)
  i, primes, nums = 2, [], [0 for i in range(2, max_num + 1)]
  while i < max_num:
    is_prime = True
    for p in primes:
      if p % i == 0:
        is_prime = False
        break
    if is_prime:
      if set([a % i for a in arr]) == no_set:
        return True
      primes.append(i)
    i += 1
  return False

def hasSubset(N, arr):
  if hasGCD(arr):
    return "NO"
  return "YES"


if __name__ == '__main__':
  T = int(raw_input())
  for i in range(T):
    N = int(raw_input())
    arr = map(int, raw_input().split())
    print hasSubset(N, arr)
