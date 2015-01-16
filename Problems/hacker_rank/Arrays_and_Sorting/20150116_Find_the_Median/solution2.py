if __name__ == '__main__':
  n = int(raw_input())
  ar = [int(i) for i in raw_input().split()]
  print sorted(ar)[n / 2]
