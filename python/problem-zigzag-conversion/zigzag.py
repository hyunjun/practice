# https://leetcode.com/problems/zigzag-conversion/

def convert(s, numRows):
  result = []
  [result.append([]) for i in range(numRows)]

  i, len_s = 0, len(s)
  while i < len_s:
    r = 0
    while r < numRows and i < len_s:
      result[r].append(s[i])
      r += 1
      i += 1
    if i < len_s:
      result[numRows - 1].append(' ')
      r = numRows - 2
    while 0 < r and i < len_s:
      result[r].append(s[i])
      r -= 1
      i += 1
    if i < len_s:
      result[0].append(' ')
  return ''.join([''.join([c for c in r if c != ' ']) for r in result])

data = 'PAYPALISHIRING'
print(convert(data, 3))