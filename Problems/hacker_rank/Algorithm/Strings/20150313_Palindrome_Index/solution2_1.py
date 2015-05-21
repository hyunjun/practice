def is_palindrome(s, not_checking_idx=-1):
  l, r = 0, len(s) - 1
  while l < r:
    if l == not_checking_idx:
      l += 1
    if r == not_checking_idx:
      r -= 1
    if s[l] != s[r]:
      return False
    l += 1
    r -= 1
  return True

def palindrome_index(s):
  if is_palindrome(s):
    return -1
  str_len = len(s)
  for i in range(str_len):
    if is_palindrome(s, i):
      return i
  return 0

if __name__ == '__main__':
  n = int(raw_input())
  for i in range(n):
    print palindrome_index(raw_input())
