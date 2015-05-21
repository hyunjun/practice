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
  def around_points(dots, point):
    #print 'point', point
    results = []
    if 0 < len(dots):
      nexts, r, c = [], point[0], point[1]
      if 0 < c:
        if (r, c - 1) in dots:
          dots.remove((r, c - 1))
          nexts.append((r, c - 1))
          #print 'nexts', nexts
      if 0 < r:
        if (r - 1, c) in dots:
          dots.remove((r - 1, c))
          nexts.append((r - 1, c))
          #print 'nexts', nexts
      if c < max_col:
        if (r, c + 1) in dots:
          dots.remove((r, c + 1))
          nexts.append((r, c + 1))
          #print 'nexts', nexts
      if r < max_row:
        if (r + 1, c) in dots:
          dots.remove((r + 1, c))
          nexts.append((r + 1, c))
          #print 'nexts', nexts
      for n in nexts:
        results.extend(around_points(dots, n))
    results.append(point)
    return results

  dots = []
  for r in range(max_row):
    for c in range(max_col):
      if '.' == land[r][c]:
        dots.append((r, c))
  #print 'all dots', dots
  dot_sets = []
  while 0 < len(dots):
    dot_sets.append(around_points(dots, dots.pop(0)))
  size = -1
  for dot_set in dot_sets:
    if len(dot_set) < 4:
      continue
    min_row, max_row, min_col, max_col = min([r for r, c in dot_set]), max([r for r, c in dot_set]), min([c for r, c in dot_set]), max([c for r, c in dot_set])
    if min_row == max_row or min_col == max_col:
      continue
    size = max(size, _size_of_fence(land, min_row, max_row, min_col, max_col))
    #print 'dot_set', dot_set, min_row, max_row, min_col, max_col, _size_of_fence(land, min_row, max_row, min_col, max_col)
  if size == -1:
    return 'impossible'
  return size


if __name__ == '__main__':
  ROW, COL = map(int, raw_input().split())
  LAND = [''] * ROW
  for r in range(ROW):
    LAND[r] = raw_input()
  print size_of_fence(LAND, ROW, COL)
