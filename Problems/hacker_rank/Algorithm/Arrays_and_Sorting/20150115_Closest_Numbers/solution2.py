def print_pair(pairs):
  print ' '.join(['{} {}'.format(a, b) for a, b in pairs])


def closest_numbers(ar):
  ar = sorted(ar)
  pairs = zip(ar[1:], ar[:-1])
  min_diff = min([a - b for a, b in pairs])
  return [(b, a) for a, b in pairs if min_diff == a - b]


if __name__ == '__main__':
  n = int(raw_input())
  ar = [int(i) for i in raw_input().split()]
  print_pair(closest_numbers(ar))
