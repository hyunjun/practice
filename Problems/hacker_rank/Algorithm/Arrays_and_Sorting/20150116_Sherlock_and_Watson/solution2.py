def right_rotation(ar, k):
  idx = len(ar) - k % len(ar)
  return ar[idx:] + ar[:idx]

if __name__ == '__main__':
  N, K, Q = map(int, raw_input().split())
  ar = [int(i) for i in raw_input().split()]
  ar = right_rotation(ar, K)
  for i in range(Q):
    print ar[int(raw_input())]
