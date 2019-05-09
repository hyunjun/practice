#   https://www.educative.io/collection/page/5668639101419520/5671464854355968/5652017242439680


class interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return '[{}, {}]'.format(self.start, self.end)

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


def merge(intervals):
    if intervals is None or 0 == len(intervals):
        return []
    intervals.sort(key=lambda t: (t.start, t.end))
    p, c = 0, 1
    while c < len(intervals):
        s1, e1 = intervals[p].start, intervals[p].end
        s2, e2 = intervals[c].start, intervals[c].end
        if e1 >= s2:
            if e1 == s2:
                ms, me = s1, e2
            elif s1 == s2:
                if e1 <= e2:
                    ms, me = s1, e2
            elif s1 < s2:
                if e1 >= e2:
                    ms, me = s1, e1
                else:
                    ms, me = s1, e2
            intervals[p].start, intervals[p].end = None, None
            intervals[c].start, intervals[c].end = ms, me
        p += 1
        c += 1
    return [i for i in intervals if i.start is not None and i.end is not None]


data = [([interval(1, 4), interval(2, 5), interval(7, 9)], [interval(1, 5), interval(7, 9)]),
        ([interval(6, 7), interval(2, 4), interval(5, 9)], [interval(2, 4), interval(5, 9)]),
        ([interval(1, 4), interval(2, 6), interval(3, 5)], [interval(1, 6)]),
        ]
for intervals, expected in data:
    real = merge(intervals)
    print('{}, expected {}, real {}, result {}'.format(intervals, expected, real, expected == real))
