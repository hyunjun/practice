def counting_sort(ar):
  res = {}
  for x, s in ar:
    res.setdefault(x, []).append(s)
  return ' '.join([' '.join(words) for x, words in res.items()])
  
if __name__ == '__main__':
  n, ar = int(input()), []
  for i in range(n):
    x, s = input().split()
    x = int(x)
    if i < n / 2:
      ar.append((x, '-'))
    else:
      ar.append((x, s))
  print(counting_sort(ar))
