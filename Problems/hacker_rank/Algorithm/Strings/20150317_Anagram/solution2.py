# https://www.hackerrank.com/challenges/anagram
from collections import Counter

def number_of_changes(s):
  l = len(s)
  if l % 2 == 1:
    return -1
  n, d1, d2 = 0, Counter(s[:l / 2]), Counter(s[l / 2:])
  for i in range(97, 97 + 26):
    c = chr(i)
    if c in d1 and c in d2:
      n += abs(d1[c] - d2[c])
    elif c in d1:
      n += d1[c]
    elif c in d2:
      n += d2[c]
  return n / 2

if __name__ == '__main__':
  n = int(raw_input())
  for i in range(n):
    print number_of_changes(raw_input())
