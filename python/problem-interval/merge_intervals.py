#   https://leetcode.com/problems/merge-intervals

#   https://leetcode.com/problems/merge-intervals/solution


from Interval import Interval
from Interval import intervalStrings
from typing import List


class Solution:
    #   runtime; 80ms, 23.17%
    def merge0(self, intervals):
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

    #   https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3535
    #   runtime; 96ms, 16.37%
    #   memory; 15.7MB, 89.46%
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        for i, interval in enumerate(intervals):
            if 0 == i:
                continue
            if intervals[i - 1][1] >= interval[0]:
                intervals[i] = [min(intervals[i - 1][0], interval[0]), max(intervals[i - 1][1], interval[1])]
                intervals[i - 1] = [None, None]
        return [interval for interval in intervals if interval[0] is not None and interval[1] is not None]


s = Solution()
data = [([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ]
for intervals, expected in data:
    real = s.merge(intervals)
    print('{}, expected {}, real {}, result {}'.format(intervalStrings(intervals), intervalStrings(expected), intervalStrings(real), intervalStrings(expected) == intervalStrings(real)))
