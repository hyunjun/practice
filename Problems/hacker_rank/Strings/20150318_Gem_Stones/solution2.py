from collections import Counter

def number_of_gem_stones(strs):
  d, result, num_of_strs = {}, 0, len(strs)
  for i in range(97, 97 + 26):
    c = chr(i)
    d[c] = [0] * num_of_strs
  for i, s in enumerate(strs):
    sd = Counter(s)
    for c, n in d.items():
      if c in sd:
        d[c][i] = sd[c]
  for c, n in d.items():
    if 0 not in n:
      result += 1
  return result

if __name__ == '__main__':
  strs, n = [], int(raw_input())
  for i in range(n):
    strs.append(raw_input())
  print number_of_gem_stones(strs)
