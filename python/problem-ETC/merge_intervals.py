#   https://leetcode.com/problems/merge-intervals

#   https://leetcode.com/problems/merge-intervals/solution


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[{},{}]'.format(self.start, self.end)


intervalStrings=lambda intervals: ' '.join([interval.__str__() for interval in intervals])


class Solution:
    #   23.17%
    def merge(self, intervals):
        if intervals is None or 0 == len(intervals):
            return []
        intervals = sorted(intervals, key=lambda i: (i.start, i.end))
        s, e = 0, 1
        while s < len(intervals) and e < len(intervals):
            if intervals[s].end >= intervals[e].start:
                intervals[s].end = max(intervals[s].end, intervals[e].end)
                intervals.pop(e)
            else:
                s += 1
                e += 1
        return intervals


s = Solution()
data = [([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)], [Interval(1, 6), Interval(8, 10), Interval(15, 18)]),
        ([Interval(1, 4), Interval(4, 5)], [Interval(1, 5)]),
        ]
for intervals, expected in data:
    real = s.merge(intervals)
    print('{}, expected {}, real {}, result {}'.format(intervalStrings(intervals), intervalStrings(expected), intervalStrings(real), intervalStrings(expected) == intervalStrings(real)))
