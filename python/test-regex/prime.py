import re
import sys

#  http://www.noulakaz.net/weblog/2007/03/18/a-regular-expression-to-check-for-prime-numbers/
def is_prime(n):
  s = ''
  while 0 < n:
    n -= 1
    s += '1'
  return None == re.match(re.compile('^1?$|^(11+?)\\1+$'), s)


if __name__ == '__main__':
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
    print(n, is_prime(n))
