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
  str_len = len(s)
  for i in range(str_len):
    if is_palindrome(s[:i] + s[i + 1:]):
      return i
  return 0

if __name__ == '__main__':
  n = int(raw_input())
  for i in range(n):
    print palindrome_index(raw_input())
