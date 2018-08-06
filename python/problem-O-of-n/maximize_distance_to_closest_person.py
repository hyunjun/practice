#   https://leetcode.com/problems/maximize-distance-to-closest-person

#   https://leetcode.com/problems/maximize-distance-to-closest-person/solution


class Solution:
    #   12.92%
    def maxDistToClosest(self, seats):
        maxDist = 0
        if 0 == seats[0]:
            i = seats.index(1)
            maxDist = max(maxDist, i)
        s, e, lastOneIdx = 0, 0, -1
        for i, seat in enumerate(seats):
            if 1 == seat:
                lastOneIdx = i
            if 0 == i:
                continue
            if seats[i - 1] == 1 and seat == 0:
                s = i
            elif seats[i - 1] == 0 and seat == 1:
                maxDist = max(maxDist, (i - 1 + s) // 2 - s + 1)
        if 0 == seats[-1] and -1 != lastOneIdx:
            maxDist = max(maxDist, len(seats) - 1 - lastOneIdx)
        return maxDist


s = Solution()
data = [([1, 0, 0, 0, 1, 0, 1], 2),
        ([1, 0, 0, 0], 3),
        ([0, 0, 0, 1], 3),
        ([0, 1], 1),
        ([0, 1, 0, 0], 2),
        ]
for seats, expected in data:
    real = s.maxDistToClosest(seats)
    print('{}, expected {}, real {}, result {}'.format(seats, expected, real, expected == real))
