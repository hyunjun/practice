if __name__ == '__main__':
  word, N = 'hackerrank', int(raw_input())
  for i in range(N):
    start, end, s = False, False, raw_input()
    if s.startswith(word):
      start = True
    if s.endswith(word):
      end = True
    if start and end:
      print '0'
    elif start:
      print '1'
    elif end:
      print '2'
    else:
      print '-1'
