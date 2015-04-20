if __name__ == '__main__':
  inps = [int(n) for n in raw_input().split()]
  r, c = inps[0] - 1, inps[1] - 1
  if r % 2 == 0:
    print [10 * (r / 2) + n for n in range(0, 10, 2)][c]
  else:
    print [10 * (r / 2) + n for n in range(1, 10, 2)][c]
