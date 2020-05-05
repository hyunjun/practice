#   https://codebasil.com/problems/bad-day-at-school


def badDayAtSchool(intervals):
    merged = []
    for s, e in sorted(intervals):
        if 0 == len(merged) or merged[-1][1] < s:
            merged.append([s, e])
        else:
            merged[-1] = [min(merged[-1][0], s), max(merged[-1][1], e)]
    return sorted(merged)


data = [([[800, 1100], [1300, 1400], [1000, 1200], [1050, 1250], [1350, 1500]], [[800, 1250], [1300, 1500]]),
        ([[800, 800], [1000, 1000], [1240, 1260], [900, 1100], [1241, 1300]], [[800, 800], [900, 1100], [1240, 1300]]),
        ]
for intervals, expected in data:
    real = badDayAtSchool(intervals)
    print(f'{intervals} expected {expected} real {real} result {expected == real}')
