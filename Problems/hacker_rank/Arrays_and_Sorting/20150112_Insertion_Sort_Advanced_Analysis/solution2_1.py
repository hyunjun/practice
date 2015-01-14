# http://www.quora.com/How-can-I-efficiently-compute-the-number-of-swaps-required-by-slow-sorting-methods-like-insertion-sort-and-bubble-sort-to-sort-a-given-array
# http://183.106.113.109/30stair/bindexedtree/bindexedtree.php?pname=bindexedtree

class Bit:
  def __init__(self, n):
    sz = 1
    while n > sz:
      sz *= 2
    self.size = sz
    self.data = [0] * sz

  def sum(self, i):
    s = 0
    while i > 0:
      s += self.data[i]
      i -= i & -i
    return s

  def add(self, i, x):
    while i < self.size:
      self.data[i] += x
      i += i & -i

def inversions(arr):
  res = 0
  bit = Bit(max(arr) + 1)
  for i, v in enumerate(arr):
    print 'i {} bit.sum({}) {} - bit.sum({}) = {}'.format(i, v, i, v, bit.sum(v))
    res += i - bit.sum(v)
    print 'res {}'.format(res)
    bit.add(v, 1)
    print bit.data
  return res


if __name__ == '__main__':
  for i in range(int(raw_input())):
    n = int(raw_input())
    arr = [int(i) for i in raw_input().split()]
    print inversions(arr)
