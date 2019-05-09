#   https://www.educative.io/collection/page/5668639101419520/5671464854355968/5718314357620736


def insert(intervals, new_interval):
    if intervals is None or 0 == len(intervals):
        return []
    intervals.append(new_interval)
    intervals.sort()
    p, c, removed = 0, 1, []
    while c < len(intervals):
        s1, e1 = intervals[p]
        s2, e2 = intervals[c]
        if s2 <= e1:
            intervals[c] = [min(s1, s2), max(e1, e2)]
            removed.append(p)
        p += 1
        c += 1
    return [interval for i, interval in enumerate(intervals) if i not in removed]


data = [([[1,3], [5,7], [8,12]], [4,6], [[1,3], [4,7], [8,12]]),
        ([[1,3], [5,7], [8,12]], [4,10], [[1,3], [4,12]]),
        ([[2,3],[5,7]], [1,4], [[1,4], [5,7]]),
        ]
for intervals, new_interval, expected in data:
    real = insert(intervals, new_interval)
    print('{}, {}, expected {}, real {}, result {}'.format(intervals, new_interval, expected, real, expected == real))
