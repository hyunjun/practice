#   https://leetcode.com/problems/interval-list-intersections

#   https://leetcode.com/problems/interval-list-intersections/solution


from typing import List


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
    def intervalIntersection0(self, A, B):
        if A is None or 0 == len(A) or B is None or 0 == len(B):
            return []
        ai, bi, res = 0, 0, []
        while ai < len(A) and bi < len(B):
            sa, ea = A[ai].start, A[ai].end
            sb, eb = B[bi].start, B[bi].end
            #print('A[{}] = {}, {}\tB[{}] = {}, {}'.format(ai, sa, ea, bi, sb, eb))
            if ea == sb:
                res.append(Interval(ea, ea))
            elif sa == eb:
                res.append(Interval(eb, eb))
            else:
                if not (sa < ea < sb < eb or sb < eb < sa < ea):
                    res.append(Interval(max(sa, sb), min(ea, eb)))
            if ea < eb:
                ai += 1
                #print('ea {} < eb {} ai {} bi {}'.format(ea, eb, ai, bi))
            elif ea > eb:
                bi += 1
                #print('ea {} > eb {} ai {} bi {}'.format(ea, eb, ai, bi))
            else:
                ai += 1
                bi += 1
                #print('ea {} == eb {} ai {} bi {}'.format(ea, eb, ai, bi))
        return res

    #   https://leetcode.com/submissions/detail/343498293/?from=/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3338
    #   runtime; 172ms, 25.02%
    #   memory; 14.4MB
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if A is None or not (1 <= len(A) <= 1000) or B is None or not (1 <= len(B) <= 1000):
            return []
        res, a, b = [], 0, 0
        while a < len(A) and b < len(B):
            if A[a][0] <= B[b][0] <= A[a][1] or B[b][0] <= A[a][0] <= B[b][1]:
                res.append([max(A[a][0], B[b][0]), min(A[a][1], B[b][1])])
            if A[a][1] < B[b][1]:
                a += 1
            elif A[a][1] > B[b][1]:
                b += 1
            else:
                a += 1
                b += 1
        return res
                


s = Solution()
data = [([Interval(0,2), Interval(5,10), Interval(13,23), Interval(24,25)], [Interval(1,5), Interval(8,12), Interval(15,24), Interval(25,26)], [Interval(1,2), Interval(5,5), Interval(8,10), Interval(15,23), Interval(24,24), Interval(25,25)]),
        ]
for A, B, expected in data:
    real = s.intervalIntersection0(A, B)
    print('{}, {}, expected {}, real {}, result {}'.format(A, B, expected, real, expected == real))

data = [([[0,2], [5,10], [13,23], [24,25]], [[1,5], [8,12], [15,24], [25,26]], [[1,2], [5,5], [8,10], [15,23], [24,24], [25,25]]),
        ]
for A, B, expected in data:
    real = s.intervalIntersection(A, B)
    print('{}, {}, expected {}, real {}, result {}'.format(A, B, expected, real, expected == real))
