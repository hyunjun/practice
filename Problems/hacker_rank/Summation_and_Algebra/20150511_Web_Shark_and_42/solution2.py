M = 10**9 + 7

if __name__ == '__main__':
  T = int(raw_input())
  for i in range(T):
    '''
    # right, but slow
    s, S = 1, int(raw_input())
    while S > 0:
      s += 1
      if (s % 2 == 0 or s % 4 == 0) and s % 42 != 0:
        S -= 1
    print s % M
    '''
    div_42, prev_div_42, S = 0, 0, int(raw_input()) * 2
    div_42 = S / 42
    while div_42 != prev_div_42:
      S = S + (div_42 - prev_div_42) * 2
      prev_div_42 = div_42
      div_42 = S / 42
    print S % M
