from collections import OrderedDict

def is_palindrome(s):
  l, r = 0, len(s) - 1
  while l < r:
    if s[l] != s[r]:
      return False
    l += 1
    r -= 1
  return True

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
  n = int(input())
  for i in range(n):
    print(palindrome_index(input()))
