def num2bit(n):
  bit, bits = 1, []
  while bit <= n:
    if bit & n:
      bits.append(1)
    else:
      bits.append(0)
    bit <<= 1
  return bits


def hasSubset(N, arr):
  i, cnt, nonSet = 1, 2 ** len(arr), set([0])
  while i < cnt:
    # bits = num2bit(i)
    # bits_len = len(bits)
    # print int(i, 2)
    '''
    subset = [a for j, a in enumerate(arr[:bits_len]) if bits[j] == 1]
    # print subset
    # if 1 in subset:
    #  return 'YES'
    to = min(subset) + 1
    # print '\t', subset, 'check from 2 to', to
    for d in range(2, to):
      # print '\t\t', set([s % d for s in subset]) == nonSet
      if set([s % d for s in subset]) == nonSet:
        break
      else:
        return 'YES'
    '''
    i += 1
  return 'NO'


if __name__ == '__main__':
  T = int(raw_input())
  for i in range(T):
    N = int(raw_input())
    arr = map(int, raw_input().split())
    print hasSubset(N, arr)
