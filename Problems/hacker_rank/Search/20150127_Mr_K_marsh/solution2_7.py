def size_of_fence(LAND, M, N):
  LEFT, SIZES = [], []
  [LEFT.append([0] * N) for r in range(M)]
  [SIZES.append([0] * N) for r in range(M)]
  for r in range(M):
    if LAND[r][0] == 'x':
      LEFT[r][0] = -1
  for r in range(M):
    for c in range(1, N):
      if LAND[r][c] == 'x':
        #LEFT[r][c] = LEFT[r][c - 1] - 1
        LEFT[r][c] = -1
      else:
        LEFT[r][c] = LEFT[r][c - 1] + 1
  print 'LEFT'
  for r in range(M):
    print LEFT[r]

  size = 0
  for r in range(1, M):
    for c in range(1, N):
      if LEFT[r][c] < 0:
        continue
      max_col_size = LEFT[r][c]
      row_idx = r - 1
      fence_size = -1
      while 0 <= row_idx and 0 <= LEFT[row_idx][c]:
        col_size = min(max_col_size, LEFT[row_idx][c])
        if 0 < col_size:
          cur_fence_size = col_size * 2
          if 0 < r - row_idx:
            cur_fence_size += 2 * (r - row_idx)
          fence_size = max(fence_size, cur_fence_size)
          print '{}, {} ~ {}, {} col_size {} row_size {} total {}'.format(row_idx, c, r, c, col_size, r - row_idx, cur_fence_size)
        #else:
        #  if LAND[row_idx][c - max_col_size] == 'x':
        #    break
        row_idx -= 1
      SIZES[r][c] = fence_size
      size = max(size, fence_size)

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
