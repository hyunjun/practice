def size_of_fence(LAND, M, N):
  COL, ROW = [], []
  for r in range(M):
    COL.append([-1] * N)
    ROW.append([-1] * N)
  for r in range(1, M):
    if LAND[r][0] != 'x':
      ROW[r][0] = ROW[r - 1][0] + 1
  for c in range(1, N):
    if LAND[0][c] != 'x':
      COL[0][c] = COL[0][c - 1] + 1
  for r in range(1, M):
    for c in range(1, N):
      if LAND[r][c] != 'x':
        COL[r][c] = COL[r][c - 1] + 1
        ROW[r][c] = ROW[r - 1][c] + 1
  size, col_diff, row_diff = 0, [-1] * N, [-1] * N
  for r1 in range(M - 1):
    for r2 in range(r1 + 1, M):
      for c in range(N):
        if 'x' == LAND[r2][c] or 'x' == LAND[r1][c]:
          col_diff[c], row_diff[c] = -1000, -1000
        else:
          col_diff[c] = COL[r2][c] - COL[r1][c]
          row_diff[c] = ROW[r2][c] - ROW[r1][c]
      l, r, i, rdiff = -1, -1, 0, r2 - r1
      while i < N - 1:
        if l == -1:
          l = r = i
          while r < N and col_diff[r] != -1000 and col_diff[r] == col_diff[l]:
            r += 1
          if l + 1 < r:
            rl, rr = l, r - 1
            while row_diff[rl] != rdiff and rl < rr:
              rl += 1
            while row_diff[rr] != rdiff and rl < rr:
              rr -= 1
            if rl < rr:
              size = max(size, (rdiff + rr - rl) * 2)
          i += r - l + 1
          l = -1
        else:
          i += 1

  if size == 0:
    return 'impossible'
  return size

if __name__ == '__main__':
  M, N = map(int, raw_input().split())
  LAND = [''] * M
  for r in range(M):
    LAND[r] = raw_input()
  print size_of_fence(LAND, M, N)
