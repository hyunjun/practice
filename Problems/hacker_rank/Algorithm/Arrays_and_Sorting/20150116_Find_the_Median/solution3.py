if __name__ == '__main__':
  n = int(input())
  ar = [int(i) for i in input().split()]
  print(sorted(ar)[int(n / 2)])
