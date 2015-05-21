if __name__ == '__main__':
  T = int(raw_input())
  for i in range(T):
    inps = [int(n) for n in raw_input().split()]
    l, b = inps[0], inps[1]
    for s in range(min(l, b), 0, -1):
      if l % s == 0 and b % s == 0:
        print (l / s) * (b / s)
        break
