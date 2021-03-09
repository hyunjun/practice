def counting_sort(ar):
  counts = [0] * 100
  for x, s in ar:
    counts[x] += 1
  for i in range(1, 100):
    if 0 < counts[i]:
      counts[i] += counts[i - 1]
    elif 0 == counts[i]:
      counts[i] = counts[i - 1]
  return counts


if __name__ == '__main__':
  n, ar = int(input()), []
  for i in range(n):
    x, s = input().split()
    x = int(x)
    ar.append((x, s))
  print(" ".join([str(r) for r in counting_sort(ar)]))
