from collections import OrderedDict

def is_palindrome(s):
  str_len = len(s)
  m = str_len / 2
  if str_len % 2 == 0:
    if s[:m] == s[:m - 1:-1]:
      return True
  else:
    if s[:m] == s[:m:-1]:
      return True
  return False

def palindrome_index(s):
  if is_palindrome(s):
    return -1

  alpha_dict = {}
  [alpha_dict.setdefault(c, []).append(i) for i, c in enumerate(s)]
  sorted_alpha_dict = OrderedDict(sorted(alpha_dict.items(), key=lambda t: len(t[1])))
  for c, idx_list in sorted_alpha_dict.items():
    if len(idx_list) % 2 == 1:
      for i in idx_list:
        if is_palindrome(s[:i] + s[i + 1:]):
          return i
  return 0

if __name__ == '__main__':
  n = int(raw_input())
  for i in range(n):
    print palindrome_index(raw_input())
