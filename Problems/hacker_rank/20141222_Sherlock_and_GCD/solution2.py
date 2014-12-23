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
  for i in range(1, 2 ** len(arr)):
    bits = num2bit(i)
    subset = [a for j, a in enumerate(arr[:len(bits)]) if bits[j] == 1]
    if 1 in subset:
      return 'YES'
    if 0 < len([i for i in map(lambda x: x % subset[0], subset) if i is not 0]):
      return 'YES'
  return 'NO'


if __name__ == '__main__':
  T = int(raw_input())
  for i in range(T):
    N = int(raw_input())
    arr = map(int, raw_input().split())
    print hasSubset(N, arr)
