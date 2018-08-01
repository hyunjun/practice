# https://leetcode.com/problems/implement-strstr/

def strstr(haystack, needle):
  if haystack is None or needle is None:
    return -1

  if haystack == needle:
    return 0

  len_haystack = len(haystack)
  len_needle = len(needle)
  if 0 == len_needle:
    return 0

  if 0 == len_haystack or len_haystack < len_needle:
    return -1

  print('len haystack {} needle {}'.format(len_haystack, len_needle))
  for i in range(len_haystack - len_needle + 1):
    if haystack[i] == needle[0]:
      if haystack[i : i + len_needle] == needle:
        return i
  return -1

cases = [('abcdefghi', 'cde', 2), ('abcdefghi', 'cdf', -1), ('abcdecabcd', 'cab', 5), ('abcdecabcd', 'cac', -1), ('', '', 0), ('a', '', 0), ("mississippi", "pi", 9)]
for haystack, needle, expected in cases:
  print('haystack {}\tneedle {}\texpected {}\treal {}'.format(haystack, needle, expected, strstr(haystack, needle)))