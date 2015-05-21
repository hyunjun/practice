def size_of_fence(LAND, M, N):
  LEFT, TOP, SIZES = [], [], []
  [LEFT.append([0] * N) for r in range(M)]
  [TOP.append([0] * N) for r in range(M)]
  [SIZES.append([0] * N) for r in range(M)]
  for r in range(1, M):
    if LAND[r][0] == 'x':
      LEFT[r][0] = -1
  for c in range(1, N):
    if LAND[0][c] == 'x':
      TOP[0][c] = -1
  for r in range(1, M):
    for c in range(1, N):
      if LAND[r][c] == 'x':
        #LEFT[r][c] = LEFT[r][c - 1] - 1
        #TOP[r][c] = TOP[r - 1][c] - 1
        LEFT[r][c] = -1
        TOP[r][c] = -1
      else:
        LEFT[r][c] = LEFT[r][c - 1] + 1
        TOP[r][c] = TOP[r - 1][c] + 1
  print 'LEFT'
  for r in range(M):
    print LEFT[r]
  print 'TOP'
  for r in range(M):
    print TOP[r]
  '''for r1 in range(0, M - 1):
    for r2 in range(r1 + 1, M):
      rdiff = r2 - r1
      for c1 in range(0, N - 1):
        for c2 in range(c1 + 1, N):
          if TOP[r2][c2] < rdiff or LEFT[r2][c2] < c2 - c1:
            continue
          print 'calc size of ({}, {})~({}, {})'.format(r1, c1, r2, c2)
          SIZES[r2][c2] = (TOP[r2][c2] + 1) * (LEFT[r2][c2] + 1)'''
  '''size = 0
  for r in range(1, M):
    for c in range(1, N):
      if 0 < LEFT[r][c] and 0 < TOP[r][c]:
        SIZES[r][c] = 2 * (TOP[r][c] + LEFT[r][c])
        size = max(size, SIZES[r][c])'''

  size = 0
  for r1 in range(M - 1):
    for r2 in range(r1 + 1, M):
      rdiff = r2 - r1
      max_col_size = LEFT[r2][1]
      for c in range(1, N):
        if TOP[r2][c] < rdiff:
          continue
        max_col_size = max(max_col_size, LEFT[r2][c])
        SIZES[r2][c] = 2 * (TOP[r2][c] + max_col_size)

  print 'SIZE'
  for r in range(M):
    print SIZES[r]

  if size == 0:
    return 'impossible'
  return size


if __name__ == '__main__':
  M, N = map(int, raw_input().split())
  LAND = [''] * M
  for r in range(M):
    LAND[r] = raw_input()
  print size_of_fence(LAND, M, N)
