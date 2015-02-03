import math

if __name__ == '__main__':
  inp = raw_input()
  l = len(inp)
  L = math.sqrt(l)
  ROW, COL = int(L), int(L)
  while ROW * COL < l:
    COL += 1
    if ROW * COL < l:
      ROW += 1
  s, matrix = 0, []
  while s < l:
    matrix.append(inp[s:s + COL])
    s += COL
  if len(matrix[ROW - 1]) < COL:
    matrix[ROW - 1] += ' ' * (COL - len(matrix[ROW - 1]))
  for c in range(COL):
    s = ''
    for r in range(ROW):
      if matrix[r][c] != ' ':
        s += matrix[r][c]
    print s,
