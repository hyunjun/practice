def counting_sort(ar):
  res = [0] * 100
  for a in ar:
    res[a] += 1
  return " ".join([str(r) for r in res])


if __name__ == '__main__':
  n = int(input())
  ar = list(map(int, input().split()))
  print(counting_sort(ar))
