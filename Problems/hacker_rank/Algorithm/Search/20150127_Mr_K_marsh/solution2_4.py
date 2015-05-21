import collections

def _size_of_fence(LAND, M, N):
  LAND_COL = [] * N
  [LAND_COL.append([LAND[row][col] for row in range(M)]) for col in range(N)]
  #print LAND
  #print LAND_COL
  size_dict = {}
  [size_dict.setdefault(m * n, []).append((m, n)) for m in range(M, 1, -1) for n in range(N, 1, -1)]
  for k, v in collections.OrderedDict(sorted(size_dict.items(), reverse=True)).items():
    for m, n in v:
      print '{} * {} = {}'.format(m, n, k)
      for r in range(M - (m - 1)):
        for c in range(N - (n - 1)):
          print '\t({}, {})~({}, {})'.format(r, c, r + m - 1, c + n - 1)
          '''if 'x' in [ LAND[r][c], LAND[r][c + n - 1], LAND[r + m - 1][c], LAND[r + m - 1][c + n - 1] ]:
            continue
          if 'x' in LAND[r][c:c + n]:
            continue
          if 'x' in LAND[r + m - 1][c:c + n]:
            continue
          if 'x' in LAND_COL[c][r:r + m]:
            continue
          if 'x' in LAND_COL[c + n - 1][r:r + m]:
            continue
          return 2 * ((m - 1) + (n - 1))'''
  return 'impossible'


def size_of_fence(LAND, M, N):
  connections = []
  [connections.append([-1] * N) for r in range(M)]
  for r in range(M):
    for c in range(N):
      if LAND[r][c] == '.':
        connections[r][c] = r * N + c
        if 0 < c and -1 < connections[r][c - 1]:
          connections[r][c] = connections[r][c - 1]
        elif 0 < r and -1 < connections[r - 1][c]:
          connections[r][c] = connections[r - 1][c]
  groups = set()
  for r in range(M):
    groups = groups.union(set(connections[r]))
  groups.remove(-1)
  for g in groups:
    dots = [(r, c) for r in range(M) for c in range(N) if connections[r][c] == g]
    size_dict = {}
    [size_dict.setdefault(m * n, []).append((m, n)) for m, n in dots]
    for k, v in collections.OrderedDict(sorted(size_dict.items(), reverse=True)).items():
      for m, n in v:
        print '{} * {} = {}'.format(m, n, k)
        for r in range(m, M - m - 1, -1):
          for c in range(n, N - n - 1, -1):
            print '\t({}, {})'.format(r, c)
            #print '\t({}, {})~({}, {})'.format(r, c, r + M - 1, c + N - 1)
            '''if 'x' in [ LAND[r][c], LAND[r][c + n - 1], LAND[r + m - 1][c], LAND[r + m - 1][c + n - 1] ]:
              continue
            if 'x' in LAND[r][c:c + n]:
              continue
            if 'x' in LAND[r + m - 1][c:c + n]:
              continue
            if 'x' in [LAND[row][c] for row in range(r, r + m)]:
              continue
            if 'x' in [LAND[row][c + n - 1] for row in range(r, r + m)]:
              continue
            return 2 * ((m - 1) + (n - 1))'''
  return 'impossible'


if __name__ == '__main__':
  ROW, COL = map(int, raw_input().split())
  LAND = [''] * ROW
  for r in range(ROW):
    LAND[r] = raw_input()
  print _size_of_fence(LAND, ROW, COL)
  print size_of_fence(LAND, ROW, COL)
