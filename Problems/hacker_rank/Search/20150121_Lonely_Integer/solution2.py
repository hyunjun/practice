from collections import Counter


if __name__ == '__main__':
  raw_input()
  print [k for k, v in Counter(raw_input().split()).items() if v == 1][0]
