MAX_SIZE = 10**6

if __name__ == '__main__':
  min_y, min_x, N = MAX_SIZE, MAX_SIZE, int(raw_input())
  for i in range(N):
    inps = [int(n) for n in raw_input().split()]
    y, x = inps[0], inps[1]
    if y < min_y:
      min_y = y
    if x < min_x:
      min_x = x
    # print y, x, '->', min_y, min_x
  print min_y * min_x
