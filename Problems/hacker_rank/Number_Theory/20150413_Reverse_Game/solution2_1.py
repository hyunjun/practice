if __name__ == '__main__':
  T = int(raw_input())
  for i in range(T):
    inps = [int(n) for n in raw_input().split()]
    N, K = inps[0], inps[1]
    org = [n for n in range(N)]
    idx, l, r = 0, 0, N - 1
    while l <= r:
      if K == org[r]:
        print idx
        break
      idx += 1
      if K == org[l]:
        print idx
        break
      idx += 1
      l, r = l + 1, r - 1
