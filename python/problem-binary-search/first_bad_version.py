# https://leetcode.com/problems/first-bad-version

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
    #   20.44%
    def firstBadVersion0(self, n):
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

    #   https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316
    #   runtime; 36ms, 7.42%
    #   memory; 13.9MB
    def firstBadVersion(self, n):
        if n < 1:
            return 0
        l, r = 1, n
        while l < r:
            m = l + (r - l) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l
