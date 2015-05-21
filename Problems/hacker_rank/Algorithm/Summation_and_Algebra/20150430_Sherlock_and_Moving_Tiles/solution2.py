import math

ROOT2 = math.sqrt(2)

if __name__ == '__main__':
  inps = [int(n) for n in raw_input().split()]
  L, S1, S2 = inps[0], inps[1], inps[2]
  Q = int(raw_input())
  for i in range(Q):
    q = int(raw_input())
    t = abs((L * ROOT2 - math.sqrt(2 * q)) / (S2 - S1))
    print '%.5f' % t

