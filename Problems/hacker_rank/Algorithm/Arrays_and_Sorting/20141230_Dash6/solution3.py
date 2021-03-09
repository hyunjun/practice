def partition(ar):
  return [a for a in ar if a < ar[0]] + ar[:1] + [a for a in ar if ar[0] < a]


if __name__ == '__main__':
  n = int(input())
  ar = list(map(int, input().split()))
  res = partition(ar)
  print(" ".join([str(r) for r in res]))
