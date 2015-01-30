import collections

# right, but too slow
def size_of_fence(LAND, M, N):
  size_dict = {}
  [size_dict.setdefault(m * n, []).append((m, n)) for m in range(M, 1, -1) for n in range(N, 1, -1)]
  for k, v in collections.OrderedDict(sorted(size_dict.items(), reverse=True)).items():
    for m, n in v:
      #print '{} * {} = {}'.format(m, n, k)
      for r in range(M - (m - 1)):
        for c in range(N - (n - 1)):
          #print '\t({}, {})~({}, {})'.format(r, c, r + m - 1, c + n - 1)
          if 'x' in [ LAND[r][c], LAND[r][c + n - 1], LAND[r + m - 1][c], LAND[r + m - 1][c + n - 1] ]:
            continue
          if 'x' in LAND[r][c:c + n]:
            continue
          if 'x' in LAND[r + m - 1][c:c + n]:
            continue
          if 'x' in [LAND[row][c] for row in range(r, r + m)]:
            continue
          if 'x' in [LAND[row][c + n - 1] for row in range(r, r + m)]:
            continue
          return 2 * ((m - 1) + (n - 1))
  return 'impossible'

if __name__ == '__main__':
  ROW, COL = map(int, raw_input().split())
  LAND = [''] * ROW
  for r in range(ROW):
    LAND[r] = raw_input()
  print size_of_fence(LAND, ROW, COL)
