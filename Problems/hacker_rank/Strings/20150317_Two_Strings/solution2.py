# https://www.hackerrank.com/challenges/two-strings
def has_common_substring(a, b):
  for i in range(97, 97 + 26):
    c = chr(i)
    if c in a and c in b:
      return True
  return False

if __name__ == '__main__':
  n = int(raw_input())
  for i in range(n):
    a = raw_input()
    b = raw_input()
    print a, b
    if has_common_substring(a, b):
      print "YES"
    else:
      print "NO"
