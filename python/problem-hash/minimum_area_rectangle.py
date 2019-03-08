#   https://leetcode.com/problems/minimum-area-rectangle

#   https://leetcode.com/problems/minimum-area-rectangle/solution


from collections import defaultdict

class Solution:
    def minAreaRect0(self, points):
        if points is None or 0 == len(points) or 0 == len(points[0]):
            return 0
        xDict = defaultdict(set)
        for i, (x, y) in enumerate(points):
            xDict[x].add(y)
        minArea = 1600000000
        for i, x1 in enumerate(xDict.keys()):
            for j, x2 in enumerate(xDict.keys()):
                if j <= i:
                    continue
                commonY = list(xDict[x1].intersection(xDict[x2]))
                for k, y1 in enumerate(commonY):
                    for l, y2 in enumerate(commonY):
                        if l <= k:
                            continue
                        minArea = min(minArea, abs(x2 - x1) * abs(y2 - y1))
        return minArea

    #   runtime; 3892ms, 5.54%
    #   memory; 51.4MB, 5.51%
    def minAreaRect(self, points):
        if points is None or 0 == len(points) or 0 == len(points[0]):
            return 0
        xDict = defaultdict(list)
        for i, (x, y) in enumerate(points):
            xDict[x].append(y)
        ysDict = defaultdict(list)
        for x, ys in xDict.items():
            for i, y1 in enumerate(ys):
                for j, y2 in enumerate(ys):
                    if j <= i:
                        continue
                    ysDict[(min(y1, y2), max(y1, y2))].append(x)
        #print(ysDict)
        minArea = None
        for (y1, y2), xs in ysDict.items():
            for i, x1 in enumerate(xs):
                for j, x2 in enumerate(xs):
                    if j <= i:
                        continue
                    if minArea is None:
                        minArea = abs(x2 - x1) * abs(y2 - y1)
                    else:
                        minArea = min(minArea, abs(x2 - x1) * abs(y2 - y1))
        if minArea is None:
            return 0
        return minArea
        

s = Solution()
data = [([[1,1],[1,3],[3,1],[3,3],[2,2]], 4),
        ([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]], 2),
        ([[3,2],[0,0],[3,3],[3,4],[4,4],[2,1],[4,3],[1,0],[4,1],[0,2]], 1),
        ([[3,2],[3,1],[4,4],[1,1],[4,3],[0,3],[0,2],[4,0]], 0),
        ]
for points, expected in data:
    real = s.minAreaRect(points)
    print('{}, expected {}, real {}, result {}'.format(points, expected, real, expected == real))
