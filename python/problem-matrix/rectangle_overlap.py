#   https://leetcode.com/problems/rectangle-overlap

#   https://leetcode.com/problems/rectangle-overlap/solution


class Solution:
    #   Wrong Answer
    def isRectangleOverlap0(self, rec1, rec2):
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        def isIncluded(lx, ly, rx, ry, x, y):
            if lx <= x <= rx and ly <= y <= ry:
                if (lx, ly) != (x, y) and (rx, ry) != (x, y) and (lx, ry) != (x, y) and (rx, ly) != (x, y):
                    return True
            return False
        if isIncluded(x1, y1, x2, y2, x3, y3):
            return True
        if isIncluded(x1, y1, x2, y2, x3, y4):
            return True
        if isIncluded(x1, y1, x2, y2, x4, y4):
            return True
        if isIncluded(x1, y1, x2, y2, x4, y3):
            return True
        if isIncluded(x3, y3, x4, y4, x1, y1):
            return True
        if isIncluded(x3, y3, x4, y4, x1, y2):
            return True
        if isIncluded(x3, y3, x4, y4, x2, y2):
            return True
        if isIncluded(x3, y3, x4, y4, x2, y1):
            return True
        return False

    #   Time Limit Exceeded
    def isRectangleOverlap1(self, rec1, rec2):
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        def isIncluded(lx, ly, rx, ry, x, y):
            if lx < x < rx and ly < y < ry:
                return True
            return False
        for x in range(x3, x4 + 1):
            for y in range(y3, y4 + 1):
                if isIncluded(x1, y1, x2, y2, x, y):
                    return True
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if isIncluded(x3, y3, x4, y4, x, y):
                    return True
        return False

    #   4.66%
    def isRectangleOverlap(self, rec1, rec2):
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        if max(x1, x2) < min(x3, x4) or max(x3, x4) < min(x1, x2) or max(y1, y2) < min(y3, y4) or max(y3, y4) < min(y1, y2):
            return False
        def isIncluded(lx, ly, rx, ry, x, y):
            if lx < x < rx and ly < y < ry:
                return True
            return False
        step, minVal = 1, min([abs(x1), abs(y1), abs(x2), abs(y2), abs(x3), abs(y3), abs(x4), abs(y4)])
        while step < minVal:
            step *= 10
        if 1 < step:
            step //= 10
        for x in range(x3, x4 + 1, step):
            for y in range(y3, y4 + 1, step):
                if isIncluded(x1, y1, x2, y2, x, y):
                    return True
        for x in range(x1, x2 + 1, step):
            for y in range(y1, y2 + 1, step):
                if isIncluded(x3, y3, x4, y4, x, y):
                    return True
        return False


s = Solution()
data = [([0, 0, 2, 2], [1, 1, 3, 3], True),
        ([0, 0, 1, 1], [1, 0, 2, 1], False),
        ([7, 8, 13, 15], [10, 8, 12, 20], True),
        ([2, 17, 6, 20], [3, 8, 6, 20], True),
        ([-7, -3, 10, 5], [-6, -5, 5, 10], True),
        ([4, 0, 6, 6], [-5, -3, 4, 2], False),
        ([-687153884,-854669644,-368882013,-788694078], [540420176,-909203694,655002739,-577226067], False),
        ([673524460, -581219329, 832071813, 673069033], [-989327489, 444428619, 832671464, 856702204], True),
        ]
for rec1, rec2, expected in data:
    real = s.isRectangleOverlap(rec1, rec2)
    print('{}, {}, expected {}, real {}, result {}'.format(rec1, rec2, expected, real, expected == real))
