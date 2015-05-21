def is_possible_to_sort(ar):
  l, r, sorted_ar = 0, len(ar) - 1, sorted(ar)
  while l < r and ar[l] < ar[l + 1]:
    l += 1
  while 0 < r and ar[r - 1] < ar[r]:
    r -= 1
  if sorted_ar == ar[:l] + ar[r:r + 1] + ar[l + 1: r] + ar[l:l + 1] + ar[r + 1:]:
    print 'yes\nswap {} {}'.format(l + 1, r + 1)
  elif sorted_ar == ar[:l] + [i for i in reversed(ar[l: r + 1])] + ar[r + 1:]:
    print 'yes\nreverse {} {}'.format(l + 1, r + 1)
  else:
    print 'no'

if __name__ == '__main__':
  int(raw_input())
  is_possible_to_sort([int(i) for i in raw_input().split()])
