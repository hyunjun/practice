#   https://www.educative.io/collection/page/5668639101419520/5671464854355968/6518042546667520


def merge(intervals_a, intervals_b):

    def is_empty(arr):
        if arr is None or 0 == len(arr):
            return True
        return False

    if is_empty(intervals_a):
        return intervals_b
    if is_empty(intervals_b):
        return intervals_a

    def get_smaller():
        if is_empty(intervals_a) and is_empty(intervals_a):
            return [None, None]
        if is_empty(intervals_a):
            return intervals_b.pop(0)
        if is_empty(intervals_b):
            return intervals_a.pop(0)
        sa, ea = intervals_a[0]
        sb, eb = intervals_b[0]
        if sa < sb:
            return intervals_a.pop(0)
        if sa > sb:
            return intervals_b.pop(0)
        if ea < eb:
            return intervals_a.pop(0)
        return intervals_b.pop(0)

    prev, merged = get_smaller(), []
    while intervals_a or intervals_b:
        cur = get_smaller()
        if prev[1] >= cur[0]:
            merged.append([max(prev[0], cur[0]), min(prev[1], cur[1])])
        prev = cur

    p, c = 0, 1
    while c < len(merged):
        s1, e1 = merged[p]
        s2, e2 = merged[c]
        if e1 >= s2:
            merged[c] = [max(s1, s2), min(e1, e2)]
            merged.pop(p)
        else:
            p += 1
            c += 1
    return merged


data = [([[1, 3], [2, 5], [6, 9]], [[2, 3], [5, 7]], [[2, 3], [5, 5], [6, 7]]),
        ([[1, 3], [5, 7], [9, 12]], [[5, 10]], [[5, 7], [9, 10]]),
        ]
for intervals_a, intervals_b, expected in data:
    real = merge(intervals_a, intervals_b)
    print('{}, {}, expected {}, real {}, result {}'.format(intervals_a, intervals_b, expected, real, expected == real))
