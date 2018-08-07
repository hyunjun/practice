#   https://leetcode.com/problems/heaters

#   https://leetcode.com/problems/heaters/discuss/157459/Python-O(n*log(n))-binary-search


class Solution:
    #   Wrong Answer
    def findRadius0(self, houses, heaters):
        if houses is None or 0 == len(houses):
            return 0

        res = [None] * len(houses)
        heaterSet = set(heaters)
        prevHeater = -1
        for i, h in enumerate(houses):
            if h in heaterSet:
                prevHeater = h
                res[i] = 0
            else:
                if -1 != prevHeater:
                    res[i] = h - prevHeater
        print(res)
        for i in range(len(houses) - 1, -1, -1):
            if houses[i] in heaterSet:
                prevHeater = houses[i]
            else:
                if -1 != prevHeater:
                    if res[i] is None:
                        res[i] = prevHeater - houses[i]
                    else:
                        res[i] = min(res[i], abs(prevHeater - houses[i]))
        print(res)
        radius = 0
        for r in res:
            if r:
                radius = max(radius, r)
        return radius

    #   77.64%
    def findRadius(self, houses, heaters):
        if houses is None or 0 == len(houses):
            return 0

        houses = sorted(list(set(houses).union(set(heaters))))
        prevHeater, res = -1, [None] * len(houses)
        heaterSet = set(heaters)
        for i, h in enumerate(houses):
            if h in heaterSet:
                prevHeater = h
                res[i] = 0
            else:
                if -1 != prevHeater:
                    res[i] = h - prevHeater
        print(res)
        for i in range(len(houses) - 1, -1, -1):
            if houses[i] in heaterSet:
                prevHeater = houses[i]
            else:
                if -1 != prevHeater:
                    if res[i] is None:
                        res[i] = prevHeater - houses[i]
                    else:
                        res[i] = min(res[i], abs(prevHeater - houses[i]))
        print(res)
        radius = 0
        for r in res:
            if r:
                radius = max(radius, r)
        return radius


s = Solution()
data = [([1, 2, 3], [2], 1),
        ([1, 2, 3, 4], [1, 4], 1),
        ([1, 4, 6, 8], [1, 8], 3),
        ([1, 5], [2], 3),
        ]
for houses, heaters, expected in data:
    real = s.findRadius(houses, heaters)
    print('{}, {}, expected {}, real {}, result {}'.format(houses, heaters, expected, real, expected == real))
'''
res [x 0 x]
1 2 3
  2
i   h   prev    res
0   1   -1      x 0 x
1   2   1       x 0 x
2   3           x 0 1
2   3           x 0 1
1   2   1
0   1           1 0 1

1 2 3 4
1     4
0 1 2 0
0 2 1 0
i   h   prev    res
        -1      x x x x
0   1   0       0 x x x
1   2           0 1 x x
2   3           0 1 2 x
3   4   3       0 1 2 0
3   4           0 1 2 0
2   3           0 1 1 0
1   2           0 1 1 0
0   1   0

1 4 6 8
1     8
0 3 5 0
0 4 2 0
0 3 2 0
i   h   prev    res
        -1      x x x x
0   1   1       0 x x x
1   4           0 3
2   6           0 3 5 x
3   8   8       0 3 5 0
3   8           0 3 5 0
2   6           0 3 2 0
1   4           0 3 2 0
0   1   1
'''
