def print_pair(pairs):
  print(' '.join(['{} {}'.format(a, b) for a, b in pairs]))


def closest_numbers(ar):
  ar = sorted(ar)
  pairs = list(zip(ar[1:], ar[:-1]))
  min_diff = min([a - b for a, b in pairs])
  return [(b, a) for a, b in pairs if min_diff == a - b]


if __name__ == '__main__':
  n = int(input())
  ar = [int(i) for i in input().split()]
  print_pair(closest_numbers(ar))
