# https://leetcode.com/problems/first-bad-version
# 20.44%

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
'''
1, 2, ... 10
s, e = 1, 10
mid = 11 // 2 = 5 -> True
s, e = 1, 4
mid = 5 // 2 == 2 -> False
s, e = 3, 4
mid = 7 // 2 == 3 -> True
s, e = 3, 2
mid = 7 // 2 == 3 -> False
s, e = 4, 4
mid = 8 // 2 == 4 -> True
s, e = 4, 3
'''
'''
In Python I was only able to do it with a rather ugly wrapper:

def firstBadVersion(self, n):
    return bisect.bisect(type('', (), {'__getitem__': lambda self, i: isBadVersion(i)})(), False, 0, n)

Nicer, more readable version:

def firstBadVersion(self, n):
    class Wrap:
        def __getitem__(self, i):
            return isBadVersion(i)
    return bisect.bisect(Wrap(), False, 0, n)
'''


class Solution(object):
  def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
      return 0
    s, e, mid, midResult = 1, n, 0, None
    while s <= e:
      mid = (s + e) // 2
      midResult = isBadVersion(mid)
      if midResult:
        e = mid - 1
      else:
        s = mid + 1
    if midResult:
      return mid
    return mid + 1
