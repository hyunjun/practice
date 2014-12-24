def decent_number(N):
  five_start = N
  while 0 < five_start and five_start % 3 != 0:
    five_start -= 1
  three_start = N
  while 0 < three_start and three_start % 5 != 0:
    three_start -= 1
  for f in range(five_start, -1, -3):
    for t in range(three_start, -1, -5):
      if f + t == N:
        return '5' * f + '3' * t
  return -1

if __name__ == '__main__':
  T = int(raw_input())
  for i in range(T):
    print decent_number(int(raw_input()))
