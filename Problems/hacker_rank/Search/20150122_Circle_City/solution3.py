import math

if __name__ == '__main__':
  for t in range(int(input())):
    r, k = map(int, input().split())
    radius = math.sqrt(r)
    if int(radius) < radius:
      radius += 1
    radius = int(radius)
    cnt = 0
    for i in range(0, radius):
      j = math.sqrt(r - i * i)
      if int(j) == j:
        cnt += 4
    if cnt <= k:
      print('possible')
    else:
      print('impossible')
