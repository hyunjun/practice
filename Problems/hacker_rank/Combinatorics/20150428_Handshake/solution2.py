if __name__ == '__main__':
  T = int(raw_input())
  for i in range(T):
    N = int(raw_input())
    # N Combination 2 = N! / (2! * (N - 2)!)
    print N * (N - 1) / 2
