#   https://leetcode.com/problems/interval-list-intersections

#   https://leetcode.com/problems/interval-list-intersections/solution


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __repr__(self):
        return '[{}, {}]'.format(self.start, self.end)


class Solution:
    #   runtime; 100ms, 65.42%
    #   memory; 14.2MB, 5.55%
    def intervalIntersection(self, A, B):
        if A is None or 0 == len(A) or B is None or 0 == len(B):
            return []
        ai, bi, res = 0, 0, []
        while ai < len(A) and bi < len(B):
            sa, ea = A[ai].start, A[ai].end
            sb, eb = B[bi].start, B[bi].end
            print('A[{}] = {}, {}\tB[{}] = {}, {}'.format(ai, sa, ea, bi, sb, eb))
            if ea == sb:
                res.append(Interval(ea, ea))
            elif sa == eb:
                res.append(Interval(eb, eb))
            else:
                if not (sa < ea < sb < eb or sb < eb < sa < ea):
                    res.append(Interval(max(sa, sb), min(ea, eb)))
            if ea < eb:
                ai += 1
                print('ea {} < eb {} ai {} bi {}'.format(ea, eb, ai, bi))
            elif ea > eb:
                bi += 1
                print('ea {} > eb {} ai {} bi {}'.format(ea, eb, ai, bi))
            else:
                ai += 1
                bi += 1
                print('ea {} == eb {} ai {} bi {}'.format(ea, eb, ai, bi))
        return res


s = Solution()
data = [([Interval(0,2), Interval(5,10), Interval(13,23), Interval(24,25)], [Interval(1,5), Interval(8,12), Interval(15,24), Interval(25,26)], [Interval(1,2), Interval(5,5), Interval(8,10), Interval(15,23), Interval(24,24), Interval(25,25)]),
        ]
for A, B, expected in data:
    real = s.intervalIntersection(A, B)
    print('{}, {}, expected {}, real {}, result {}'.format(A, B, expected, real, expected == real))
