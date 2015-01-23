import math

if __name__ == '__main__':
  for t in range(int(raw_input())):
    r, k = map(int, raw_input().split())
    radius = math.sqrt(r)
    if int(radius) < radius:
      radius += 1
    radius = int(radius)
    # works but very slow
    #lst = range(1, l + 1)
    #if 4 + 4 * len(filter(lambda t: t[0] * t[0] + t[1] * t[1] == r, product(lst, lst))) <= k:
    cnt = 0
    for i in range(0, radius):
      j = math.sqrt(r - i * i)
      if int(j) == j:
        cnt += 4
    if cnt <= k:
      print 'possible'
    else:
      print 'impossible'
