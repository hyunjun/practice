from collections import Counter

def number_of_deletion(s1, s2):
  total, d1, d2 = 0, Counter(s1), Counter(s2)
  for i in range(97, 97 + 26):
    c = chr(i)
    total += abs(d1[c] - d2[c])
  return total

if __name__ == '__main__':
  s1 = raw_input()
  s2 = raw_input()
  print number_of_deletion(s1, s2)
