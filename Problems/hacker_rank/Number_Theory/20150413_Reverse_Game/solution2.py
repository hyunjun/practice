if __name__ == '__main__':
  T = int(raw_input())
  for i in range(T):
    inps = [int(n) for n in raw_input().split()]
    N, K = inps[0], inps[1]
    org = [n for n in range(N)]
    # too slow
    fixed, l = [], org[::-1]
    for j in range(N - 1):
      fixed.append(l.pop(0))
      print fixed, l
      l = l[::-1]
    org = fixed + l
    print org.index(K)
