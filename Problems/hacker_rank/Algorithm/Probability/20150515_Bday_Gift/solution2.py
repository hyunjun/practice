if __name__ == '__main__':
  ns, N = [], int(raw_input())
  [ns.append(int(raw_input())) for i in range(N)]
  print sum(ns) * 1.0 / 2
