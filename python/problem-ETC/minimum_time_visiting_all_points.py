#   https://leetcode.com/problems/minimum-time-visiting-all-points


class Solution(object):
    #   runtime; 1268ms, 5.30%
    #   memory; 11.8MB, 100.00%
    def minTimeToVisitAllPoints0(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        def getCount(s, e):
            c, cnt = s, 0
            while c[0] != e[0] or c[1] != e[1]:
                if c[0] < e[0]:
                    c[0] += 1
                elif c[0] > e[0]:
                    c[0] -= 1
                if c[1] < e[1]:
                    c[1] += 1
                elif c[1] > e[1]:
                    c[1] -= 1
                cnt += 1
            return cnt

        return sum([getCount(points[i - 1], points[i]) for i in range(1, len(points))])

    def minTimeToVisitAllPoints(self, points):

        #   runtime; 104ms, 5.30%
        #   memory; 11.8MB, 100.00%
        def getCount(s, e):
            xDiff, yDiff = abs(e[0] - s[0]), abs(e[1] - s[1])
            if xDiff == yDiff:
                return xDiff
            return abs(xDiff - yDiff) + min(xDiff, yDiff)

        return sum([getCount(points[i - 1], points[i]) for i in range(1, len(points))])


s = Solution()
data = [([[1,1],[3,4],[-1,0]], 7),
        ([[3,2],[-2,2]], 5),
        ([[10,3],[0,9],[-1,1000],[30,2]], 1999),
        ]
for points, expected in data:
    real = s.minTimeToVisitAllPoints(points)
    print(f'{points}, expected {expected}, real {real}, result {expected == real}')
