def size_of_fence_by_row(land, row, col):
  min_row, max_row = row, -1
  for r in range(row):
    if 'x' in land[r]:
      continue
    else:
      min_row = r
      break
  for r in range(row - 1, -1, -1):
    if 'x' in land[r]:
      continue
    else:
      max_row = r
      break
  if min_row >= max_row:
    print 'by row: min row {} max row {}'.format(min_row, max_row)
    return 'impossible'

  min_col, max_col = col, -1
  for c in range(col):
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
  for c in range(col - 1, -1, -1):
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
  #if min_row == row or max_row == -1 or min_col == col or max_col == -1 or (min_row == max_row) or (min_col == max_col):
  if min_col >= max_col:
    print 'by row: min col {} max col {}'.format(min_col, max_col)
    return 'impossible'
  print 'by row: min_row {} max_row {} min_col {} max_col {}'.format(min_row, max_row, min_col, max_col)
  return 2 * (max_row - min_row) + 2 * (max_col - min_col)

def size_of_fence_by_col(land, row, col):
  min_col, max_col = col, -1
  for c in range(col):
    has_marsh = False
    for r in range(row):
      if 'x' in land[r][c]:
        has_marsh = True
        break
    if has_marsh:
      continue
    else:
      min_col = c
      break
  for c in range(col - 1, -1, -1):
    has_marsh = False
    for r in range(row):
      if 'x' in land[r][c]:
        has_marsh = True
        break
    if has_marsh:
      continue
    else:
      max_col = c
      break
  if min_col >= max_col:
    print 'by col: min col {} max col {}'.format(min_col, max_col)
    return 'impossible'

  min_row, max_row = row, -1
  for r in range(row):
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
  for r in range(row - 1, -1, -1):
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
    print 'by col: min row {} max row {}'.format(min_row, max_row)
    return 'impossible'
  print 'by col: min_row {} max_row {} min_col {} max_col {}'.format(min_row, max_row, min_col, max_col)
  return 2 * (max_row - min_row) + 2 * (max_col - min_col)

def size_of_fence(land, row, col):
  row_result = size_of_fence_by_row(land, row, col)
  col_result = size_of_fence_by_col(land, row, col)
  if row_result == 'impossible' and col_result == 'impossible':
    return 'impossible'
  if row_result == 'impossible':
    return col_result
  if col_result == 'impossible':
    return row_result
  return max(row_result, col_result)

if __name__ == '__main__':
  ROW, COL = map(int, raw_input().split())
  LAND = [''] * ROW
  for r in range(ROW):
    LAND[r] = raw_input()
  print size_of_fence(LAND, ROW, COL)
