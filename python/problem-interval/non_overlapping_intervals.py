#   https://leetcode.com/problems/non-overlapping-intervals


from Interval import Interval
from Interval import intervalStrings
from typing import List


class Solution:
    #   Wrong Answer
    def eraseOverlapIntervals0(self, intervals):
        s, e, cnt = 0, 0, 0
        for i, interval in enumerate(sorted(intervals, key=lambda i: (i.start, i.end))):
            if 0 == i:
                s, e = interval.start, interval.end
                continue
            if s <= interval.start < e or s < interval.end <= e:
                cnt += 1
            else:
                s = min(s, interval.start)
                e = max(e, interval.end)
        return cnt

    #   Wrong Answer
    def eraseOverlapIntervals1(self, intervals):
        d = {}
        for i, interval in enumerate(intervals):
            for idx in range(interval.start, interval.end):
                if idx in d:
                    d[idx].append(i)
                else:
                    d[idx] = [i]
        overlapped = {}
        for k, idxList in d.items():
            #print(k, idxList)
            s = set(idxList)
            for idx in idxList:
                if idx not in overlapped:
                    overlapped[idx] = set()
                #print(idx, s)
                overlapped[idx] = overlapped[idx].union(s)
                overlapped[idx].remove(idx)
                #print(idx, s, overlapped[idx])
        #print('already non overlapped')
        #for idx, s in overlapped.items():
        #    if 0 == len(s):
        #        print(intervals[idx])
        cnt, removed = 0, set()
        #print('removing')
        for idx, s in sorted(overlapped.copy().items(), key=lambda t: len(t[1]), reverse=True):
            #print(idx, s, s.difference(removed))
            if 0 == len(s.difference(removed)):
                continue
            cnt += 1
            removed.add(idx)
        #print('removed', len(removed), ['({}){}'.format(idx, intervals[idx]) for idx in removed])
        return cnt

    #   81.48%
    def eraseOverlapIntervals(self, intervals):
        sortedIntervals, lastIdx, cnt = sorted(intervals, key=lambda i: (i.start, i.end)), 0, 0
        for i, interval in enumerate(sortedIntervals):
            if 0 == i:
                continue
            if sortedIntervals[lastIdx].end <= interval.start:  #   non overlapped
                lastIdx = i
            else:
                if interval.end < sortedIntervals[lastIdx].end:
                    lastIdx = i
                cnt += 1
        return cnt


s = Solution()
data = [([Interval(1, 2), Interval(2, 3), Interval(3, 4), Interval(1, 3)], 1),
        ([Interval(1, 2), Interval(1, 2), Interval(1, 2)], 2),
        ([Interval(1, 2), Interval(2, 3)], 0),
        ([Interval(1, 2), Interval(3, 5), Interval(3, 4), Interval(2, 3)], 1),
        ([Interval(1, 2), Interval(1, 3), Interval(1, 4), Interval(2, 3)], 2),
        ([Interval(-100,-87), Interval(-99,-44), Interval(-98,-19), Interval(-97,-33), Interval(-96,-60), Interval(-95,-17), Interval(-94,-44), Interval(-93,-9), Interval(-92,-63), Interval(-91,-76), Interval(-90,-44), Interval(-89,-18), Interval(-88,10), Interval(-87,-39), Interval(-86,7), Interval(-85,-76), Interval(-84,-51), Interval(-83,-48), Interval(-82,-36), Interval(-81,-63), Interval(-80,-71), Interval(-79,-4), Interval(-78,-63), Interval(-77,-14), Interval(-76,-10), Interval(-75,-36), Interval(-74,31), Interval(-73,11), Interval(-72,-50), Interval(-71,-30), Interval(-70,33), Interval(-69,-37), Interval(-68,-50), Interval(-67,6), Interval(-66,-50), Interval(-65,-26), Interval(-64,21), Interval(-63,-8), Interval(-62,23), Interval(-61,-34), Interval(-60,13), Interval(-59,19), Interval(-58,41), Interval(-57,-15), Interval(-56,35), Interval(-55,-4), Interval(-54,-20), Interval(-53,44), Interval(-52,48), Interval(-51,12), Interval(-50,-43), Interval(-49,10), Interval(-48,-34), Interval(-47,3), Interval(-46,28), Interval(-45,51), Interval(-44,-14), Interval(-43,59), Interval(-42,-6), Interval(-41,-32), Interval(-40,-12), Interval(-39,33), Interval(-38,17), Interval(-37,-7), Interval(-36,-29), Interval(-35,24), Interval(-34,49), Interval(-33,-19), Interval(-32,2), Interval(-31,8), Interval(-30,74), Interval(-29,58), Interval(-28,13), Interval(-27,-8), Interval(-26,45), Interval(-25,-5), Interval(-24,45), Interval(-23,19), Interval(-22,9), Interval(-21,54), Interval(-20,1), Interval(-19,81), Interval(-18,17), Interval(-17,-10), Interval(-16,7), Interval(-15,86), Interval(-14,-3), Interval(-13,-3), Interval(-12,45), Interval(-11,93), Interval(-10,84), Interval(-9,20), Interval(-8,3), Interval(-7,81), Interval(-6,52), Interval(-5,67), Interval(-4,18), Interval(-3,40), Interval(-2,42), Interval(-1,49), Interval(0,7), Interval(1,104), Interval(2,79), Interval(3,37), Interval(4,47), Interval(5,69), Interval(6,89), Interval(7,110), Interval(8,108), Interval(9,19), Interval(10,25), Interval(11,48), Interval(12,63), Interval(13,94), Interval(14,55), Interval(15,119), Interval(16,64), Interval(17,122), Interval(18,92), Interval(19,37), Interval(20,86), Interval(21,84), Interval(22,122), Interval(23,37), Interval(24,125), Interval(25,99), Interval(26,45), Interval(27,63), Interval(28,40), Interval(29,97), Interval(30,78), Interval(31,102), Interval(32,120), Interval(33,91), Interval(34,107), Interval(35,62), Interval(36,137), Interval(37,55), Interval(38,115), Interval(39,46), Interval(40,136), Interval(41,78), Interval(42,86), Interval(43,106), Interval(44,66), Interval(45,141), Interval(46,92), Interval(47,132), Interval(48,89), Interval(49,61), Interval(50,128), Interval(51,155), Interval(52,153), Interval(53,78), Interval(54,114), Interval(55,84), Interval(56,151), Interval(57,123), Interval(58,69), Interval(59,91), Interval(60,89), Interval(61,73), Interval(62,81), Interval(63,139), Interval(64,108), Interval(65,165), Interval(66,92), Interval(67,117), Interval(68,140), Interval(69,109), Interval(70,102), Interval(71,171), Interval(72,141), Interval(73,117), Interval(74,124), Interval(75,171), Interval(76,132), Interval(77,142), Interval(78,107), Interval(79,132), Interval(80,171), Interval(81,104), Interval(82,160), Interval(83,128), Interval(84,137), Interval(85,176), Interval(86,188), Interval(87,178), Interval(88,117), Interval(89,115), Interval(90,140), Interval(91,165), Interval(92,133), Interval(93,114), Interval(94,125), Interval(95,135), Interval(96,144), Interval(97,114), Interval(98,183), Interval(99,157)], 187),
        ]
for intervals, expect in data:
    real = s.eraseOverlapIntervals(intervals)
    print(f'{intervalStrings(intervals)}, expect {expect}, real {real}, result {expect == real}')
