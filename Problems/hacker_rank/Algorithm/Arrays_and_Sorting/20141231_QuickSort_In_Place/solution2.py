def print_ar(ar):
  print " ".join([str(a) for a in ar])

def partition(ar, l, r, p):
  # print '\n\nar {}\tl [{}] -> {}\tr [{}] -> {}\tp [{}] -> {}'.format(ar, l, ar[l], r, ar[r], p, ar[p])
  while -1 < l < r:
    # print 'l [{}]'.format(l),
    while l < r and ar[l] < ar[p]:
      l += 1
    # print '-> [{}]'.format(l)
    # print 'r [{}]'.format(r),
    while l < r and ar[p] <= ar[r]:
      r -= 1
    # print '-> [{}]'.format(r)
    if l < r and ar[r] < ar[l]:
      # print 'swap [{}] <-> [{}]'.format(l, r)
      ar[l], ar[r] = ar[r], ar[l]
      l, r = l + 1, r - 1
      # print 'ar[{}] = {}\tar[{}] = {}'.format(l, ar[l], r, ar[r])
  if ar[p] < ar[l]:
    # print 'swap l [{}] <-> m [{}]'.format(l, p)
    ar[p], ar[l] = ar[l], ar[p]
  return ar, l

def quick_sort(ar):
  data = [(ar, 0, len(ar) - 1, len(ar) - 1)]
  while 0 < len(data):
    arr, l, r, p = data.pop(0)
    arr, p = partition(ar, l, r, p)
    print_ar(ar)
    # print '\nresult', arr, p
    if l < p - 1:
      # print 'left split l {} r {} p {}'.format(l, p - 1, p - 1)
      data.append((arr, l, p - 1, p - 1))
    if p + 1 < r:
      # print 'right split l {} r {} p {}'.format(p + 1, r, r)
      data.append((arr, p + 1, r, r))


if __name__ == '__main__':
  n = int(raw_input())
  ar = map(int, raw_input().split())
  quick_sort(ar)
