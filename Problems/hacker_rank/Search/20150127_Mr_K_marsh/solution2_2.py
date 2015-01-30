def _size_of_fence_by_row(land, row_from, row_to, col_from, col_to):
  min_row, max_row = row_to, -1
  for r in range(row_from, row_to):
    if 'x' in land[r]:
      continue
    else:
      min_row = r
      break
  for r in range(row_to, min_row, -1):
    if 'x' in land[r]:
      continue
    else:
      max_row = r
      break
  if min_row >= max_row:
    #print 'by row: min row {} max row {}'.format(min_row, max_row)
    return -1

  min_col, max_col = col_to, -1
  for c in range(col_from, col_to):
    has_marsh = False
    for r in range(min_row, max_row + 1):
      if 'x' in land[r][c]:
        has_marsh = True
        break
    if has_marsh:
      continue
    else:
      min_col = c
      break
  for c in range(col_to, min_col, -1):
    has_marsh = False
    for r in range(min_row, max_row + 1):
      if 'x' in land[r][c]:
        has_marsh = True
        break
    if has_marsh:
      continue
    else:
      max_col = c
      break
  if min_col >= max_col:
    #print 'by row: min col {} max col {}'.format(min_col, max_col)
    return -1
  #print 'by row: min_row {} max_row {} min_col {} max_col {}'.format(min_row, max_row, min_col, max_col)
  return 2 * (max_row - min_row) + 2 * (max_col - min_col)


def _size_of_fence_by_col(land, row_from, row_to, col_from, col_to):
  min_col, max_col = col_to, -1
  for c in range(col_from, col_to):
    has_marsh = False
    for r in range(row_from, row_to):
      if 'x' in land[r][c]:
        has_marsh = True
        break
    if has_marsh:
      continue
    else:
      min_col = c
      break
  for c in range(col_to, min_col, -1):
    has_marsh = False
    for r in range(row_from, row_to):
      if 'x' in land[r][c]:
        has_marsh = True
        break
    if has_marsh:
      continue
    else:
      max_col = c
      break
  if min_col >= max_col:
    #print 'by col: min col {} max col {}'.format(min_col, max_col)
    return -1

  min_row, max_row = row_to, -1
  for r in range(row_from, row_to):
    has_marsh = False
    for c in range(min_col, max_col + 1):
      if 'x' in land[r][c]:
        has_marsh = True
        break
    if has_marsh:
      continue
    else:
      min_row = r
      break
  for r in range(row_to, min_row, -1):
    has_marsh = False
    for c in range(min_col, max_col + 1):
      if 'x' in land[r][c]:
        has_marsh = True
        break
    if has_marsh:
      continue
    else:
      max_row = r
      break
  #if min_row == row or max_row == -1 or min_col == col or max_col == -1 or (min_row == max_row) or (min_col == max_col):
  if min_row >= max_row:
    #print 'by col: min row {} max row {}'.format(min_row, max_row)
    return -1
  #print 'by col: min_row {} max_row {} min_col {} max_col {}'.format(min_row, max_row, min_col, max_col)
  return 2 * (max_row - min_row) + 2 * (max_col - min_col)


def _size_of_fence(land, row_from, row_to, col_from, col_to):
  row_result = _size_of_fence_by_row(land, row_from, row_to, col_from, col_to)
  col_result = _size_of_fence_by_col(land, row_from, row_to, col_from, col_to)
  return max(row_result, col_result)


def size_of_fence(land, max_row, max_col):
  connections = []
  [connections.append([-1] * max_col) for r in range(max_row)]
  for r in range(max_row):
    for c in range(max_col):
      if land[r][c] == '.':
        connections[r][c] = r * max_col + c
        if 0 < c and -1 < connections[r][c - 1]:
          connections[r][c] = connections[r][c - 1]
        elif 0 < r and -1 < connections[r - 1][c]:
          connections[r][c] = connections[r - 1][c]
  groups = set()
  for r in range(max_row):
    groups = groups.union(set(connections[r]))
  groups.remove(-1)
  size = -1
  for g in groups:
    dots = [(r, c) for r in range(max_row) for c in range(max_col) if connections[r][c] == g]
    rows, cols = set([r for r, _ in dots]), set([c for _, c in dots])
    if len(dots) < 4 or 1 == len(set([r for r, _ in dots])) or 1 == len(set([c for _, c in dots])):
      continue
    board = []
    [board.append(['x'] * max_col) for r in range(max_row)]
    #print g, dots, set([r for r, _ in dots]), set([c for _, c in dots])
    for r in range(max_row):
      for c in range(max_col):
        if connections[r][c] == g:
          board[r][c] = '.'
    #for r in range(max_row):
    #  print board[r]
    size = max(size, _size_of_fence(board, min(rows), max(rows), min(cols), max(cols)))
  if size == -1:
    return 'impossible'
  return size


if __name__ == '__main__':
  ROW, COL = map(int, raw_input().split())
  LAND = [''] * ROW
  for r in range(ROW):
    LAND[r] = raw_input()
  print size_of_fence(LAND, ROW, COL)
