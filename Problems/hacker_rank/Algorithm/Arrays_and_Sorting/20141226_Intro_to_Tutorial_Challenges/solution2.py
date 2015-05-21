if __name__ == '__main__':
  V = int(raw_input())
  n = int(raw_input())
  arr = map(int, raw_input().split())
  for i, a in enumerate(arr):
    if V == a:
      print i
