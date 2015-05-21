from collections import Counter


if __name__ == '__main__':
  input()
  print([k for k, v in Counter(input().split()).items() if v == 1][0])
