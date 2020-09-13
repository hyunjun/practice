#   https://leetcode.com/problems/insert-interval

#   https://leetcode.com/problems/insert-interval/discuss/21753/O(n)-Python-solution


from typing import List


class Solution:
    #   runtime; 44ms, 98.47%
    #   memory; 14.7MB, 96.82%
    def insert0(self, intervals, newInterval):
        if intervals is None or 0 == len(intervals):
            return [newInterval]

        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals

        if intervals[-1][1] < newInterval[0]:
            intervals.append(newInterval)
            return intervals

        p, isOverlapped = len(intervals), False
        for i, interval in enumerate(intervals):
            if 0 < i and intervals[i - 1][1] < newInterval[0] and newInterval[1] < interval[0]:
                p = i
                break
            elif newInterval[0] <= interval[1]:
                intervals[i] = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
                p, isOverlapped = i, True
                break
        
        if not isOverlapped:
            intervals.insert(p, newInterval)
            return intervals

        c = p + 1
        while c < len(intervals):
            if intervals[c][0] <= intervals[p][1]:
                intervals[c] = [min(intervals[p][0], intervals[c][0]), max(intervals[p][1], intervals[c][1])]
                intervals[p] = [None, None]
            p += 1
            c += 1

        return [interval for interval in intervals if interval[0] is not None and interval[1] is not None]

    #   https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3458
    #   runtime; 92ms, 41.23%
    #   memory; 16.9MB, 97.55%
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        isInserted = False
        for i, interval in enumerate(intervals):
            if newInterval[0] < interval[0]:
                intervals.insert(i, newInterval)
                isInserted = True
                break
        if not isInserted:
            intervals.append(newInterval)
        for i, interval in enumerate(intervals):
            if 0 == i:
                continue
            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i][0], intervals[i][1] = min(intervals[i - 1][0], intervals[i][0]), max(intervals[i - 1][1], intervals[i][1])
                intervals[i - 1] = [None, None]
        return [interval for interval in intervals if interval[0] is not None and interval[1] is not None]
                

s = Solution()
data = [([[1,3],[6,9]], [2,5], [[1,5],[6,9]]),
        ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]]),
        ([[0,2],[3,3],[6,11]], [9,15], [[0,2],[3,3],[6,15]]),
        ([], [5, 7], [[5, 7]]),
        ([[3,5],[12,15]], [6,6], [[3,5],[6,6],[12,15]]),
        ([[1,3], [5,7], [8,12]], [4,6], [[1,3], [4,7], [8,12]]),
        ([[1,3], [5,7], [8,12]], [4,10], [[1,3], [4,12]]),
        ([[2,3],[5,7]], [1,4], [[1,4], [5,7]]),
        ]
for intervals, newInterval, expected in data:
    real = s.insert(intervals, newInterval)
    print('{}, {}, expected {}, real {}, result {}'.format(intervals, newInterval, expected, real, expected == real))
