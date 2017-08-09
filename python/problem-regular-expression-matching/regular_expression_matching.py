# https://leetcode.com/problems/regular-expression-matching/

def shorten(p):
  i = len(p) - 1
  result = [c for c in p]
  while 2 < i:
    j = i - 2
    if result[i] == '*' and result[j] == '*':
      if result[i - 1] == result[j - 1]:
        #print('same change\t[{}] = {}, [{}] = {}'.format(j - 1, result[j - 1], i - 1, result[i - 1]))
        result[i] = result[i - 1] = ''
        #print('same change\t{} {} {}'.format(i, j, result))
      elif result[i - 1] == '.' or result[j - 1] == '.':
        result[i] = result[i - 1] = ''
        result[j - 1] = '.'
        #print('dot change\t{} {} {}'.format(i, j, result))
      i -= 2
    else:
      i -= 1
  return ''.join(result).strip()


def isMatch(s, p):
  p = shorten(p)
  #print('shortened pattern {}'.format(p))
  return isMatchRecur(s, p)

def isMatchRecur(s, p):
  if s is None or p is None:
    return False

  if 0 == len(s) and 0 == len(p):
    return True

  if 0 < len(s) and 0 == len(p):
    return False

  if 2 <= len(p) and p[1] == '*':
    for i in range(len(s) + 1):
      result = isMatchRecur(s, p[0] * i + p[2:])
      if result:
        return True
  else:
    if 0 == len(s) or 0 == len(p):
      return False
    if p[0] == '.':
      return isMatchRecur(s[1:], p[1:])
    else:
      if s[0] == p[0]:
        return isMatchRecur(s[1:], p[1:])
  return False

for s, p, expected_result in [("aa", "a", False),
                              ("aa", "aa", True),
                              ("aaa", "aa", False),
                              ("aa", "a*", True),
                              ("aa", ".*", True),
                              ("ab", ".*", True),
                              ("aab", "c*a*b", True),
                              ('a', 'ab*', True),
                              ('', 'a', False),
                              ("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c", False),
                              ("aaa", "a*a", True),
                              ("aaaaa", "a*a*a", True),
                              ("abcaaaaaaabaabcabac", ".*ab.a.*a*a*.*b*b*", True),
                              ("abbcacbbbbbabcbaca", "a*a*.*a*.*a*.b*a*", True)]:
  result = isMatch(s, p)
  if expected_result == result:
    print('string {} pattern {} the same as {}'.format(s, p, expected_result))
  else:
    print('string {} pattern {} DIFF expected {} real {}'.format(s, p, expected_result, result))
