if __name__ == '__main__':
  V = int(input())
  n = int(input())
  arr = map(int, input().split())
  for i, a in enumerate(arr):
    if V == a:
      print(i)
