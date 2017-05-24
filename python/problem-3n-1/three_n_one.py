'''
f(N) = N / 2 if N % 2 == 0 or
       3 * N + 1 if N % 2 == 1 and N != 1
f(N) = K, K means the count of N = 1 after K iterations
e.g.  f(1) = 0
      f(6) = 8, because 6 > 3 > 10 > 5 > 16 > 8 > 4 > 2 > 1
'''

def getCount(n):
  if n == 1:
    return 0
  cnt = 0
  while n != 1:
    if n % 2 == 0:
      n /= 2
    else:
      n = 3 * n + 1
    cnt += 1
  return cnt

def getMinMax(n):
  largest = pow(2, n)
  smallest = 1
  while True:
    cnt = getCount(smallest)
    if cnt == n:
      break
    smallest += 1
  return smallest, largest

print getMinMax(3)
print getMinMax(8)
