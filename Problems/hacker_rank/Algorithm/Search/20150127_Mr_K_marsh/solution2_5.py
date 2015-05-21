def size_of_fence(LAND, M, N):
  sizes = []
  [sizes.append([0] * N) for r in range(M)]
  for r in range(M):
    for c in range(N):
      if LAND[r][c] == 'x':
        sizes[r][c] = -1
      else:
        sizes[r][c] = 2 * (r + c)
      #print sizes[r][c],
    #print

  size = -1
  for er in range(M - 1, 0, -1):
    for sr in range(0, er):
      for ec in range(N - 1, 0, -1):
        for sc in range(0, ec):
          if sizes[er][ec] < 0 or sizes[sr][sc] < 0:
            continue
          if sizes[er][ec] - sizes[sr][sc] < size:
            continue
          if 'x' in [ LAND[sr][sc], LAND[er][ec], LAND[sr][ec], LAND[er][sc] ]:
            continue
          if 'x' in LAND[sr][sc:ec]:
            continue
          if 'x' in LAND[er][sc:ec]:
            continue
          if 'x' in [LAND[row][sc] for row in range(sr, er)]:
            continue
          if 'x' in [LAND[row][ec] for row in range(sr, er)]:
            continue
          print 'from {}, {} to {}, {} = {}'.format(sr, sc, er, ec, sizes[er][ec] - sizes[sr][sc])
          size = max(size, sizes[er][ec] - sizes[sr][sc])
  if size == -1:
    return 'impossible'
  return size


if __name__ == '__main__':
  M, N = map(int, raw_input().split())
  LAND = [''] * M
  for r in range(M):
    LAND[r] = raw_input()
  print size_of_fence(LAND, M, N)
