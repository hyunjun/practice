import re

p = re.compile('[A-Z]{5}[0-9]{4}[A-Z]{1}')
def is_valid_PAN_format(s):
  m = re.match(p, s)
  if m is None:
    return False
  return True

if __name__ == '__main__':
  N = int(raw_input())
  for i in range(N):
    if is_valid_PAN_format(raw_input()):
      print 'YES'
    else:
      print 'NO'
