import math

# WRONG
if __name__ == '__main__':
  T = int(raw_input())
  for i in range(T):
    inps = [int(n) for n in raw_input().split()]
    cnt, D, P = 0, inps[0], inps[1]
    if D < 0:
      print 0
      continue
    discriminant = (D)**2 + 4*P
    if discriminant < 0:
      pass
    elif discriminant == 0:
      if D == 0:
        cnt = 1
      elif D / 2 == int(D / 2):
        cnt = 2
    else:
      x = math.sqrt(discriminant)
      if x == int(x):
        if D == 0:
          cnt = len([x / 2, -x / 2])
        else:
          candidates = [(D + x) / 2, (D - x) / 2, (-D + x) / 2, (-D - x) / 2]
          if P != 0 and 0 in candidates:
            cnt = 0
          else:
            cnt = len(candidates)
    print cnt
