from collections import Counter

if __name__ == '__main__':
  for i in range(int(raw_input())):
    n, ar = raw_input(), Counter([int(i) for i in raw_input().split()])
    print sum([i * (i - 1) for i in ar.values() if 1 < i])
