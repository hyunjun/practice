#   https://leetcode.com/problems/remove-covered-intervals

#   https://leetcode.com/problems/remove-covered-intervals/discuss/471854/Python-11-line-Using-2-key-Sorting


from typing import List


class Solution:
    #   runtime; 252ms, 10.53%
    #   memory; 12.9MB, 100.00%
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if intervals is None or not (1 <= len(intervals) <= 1000):
            return 0
        intervals.sort()
        for i, interval in enumerate(intervals.copy()):
            if 0 == i:
                continue
            j = i - 1
            while intervals[j] is None:
                j -= 1
            if intervals[j][0] <= intervals[i][0] < intervals[i][1] <= intervals[j][1]:
                intervals[i] = None
            elif intervals[i][0] <= intervals[j][0] < intervals[j][1] <= intervals[i][1]:
                intervals[j] = None
        return len([interval for interval in intervals if interval])


s = Solution()
data = [([[1, 4], [3, 6], [2, 8]], 2),
        ([[1, 4], [3, 6], [2, 8], [5, 9], [4, 5], [3, 4], [2, 7]], 3),
        ]
for intervals, expected in data:
    real = s.removeCoveredIntervals(intervals)
    print(f'{intervals} expected {expected} real {real} result {expected == real}')
