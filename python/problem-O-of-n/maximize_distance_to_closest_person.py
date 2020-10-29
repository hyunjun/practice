#   https://leetcode.com/problems/maximize-distance-to-closest-person

#   https://leetcode.com/problems/maximize-distance-to-closest-person/solution


from typing import List


class Solution:
    #   runtime; 88ms, 12.92%
    def maxDistToClosest0(self, seats):
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

    #   https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/563/week-5-october-29th-october-31st/3512
    #   runtime; 144ms, 46.81%
    #   memory; 14.6MB
    def maxDistToClosest(self, seats: List[int]) -> int:
        if seats is None or len(seats) < 2:
            return 0
        cnt, maxCnt, maxIdx, startCnt, endCnt = [0] * len(seats), 0, 0, 0, 0
        for i, s in enumerate(seats):
            if 0 == i or s == 1:
                continue
            cnt[i] = cnt[i - 1] + 1
            if maxCnt < cnt[i]:
                maxCnt, maxIdx = cnt[i], i
        endCnt = cnt[-1]
        for i in range(len(seats) - 1, -1, -1):
            if i == len(seats) - 1 or seats[i] == 1:
                cnt[i] = 0
                continue
            cnt[i] = cnt[i + 1] + 1
            if maxCnt < cnt[i]:
                maxCnt, maxIdx = cnt[i], i
        startCnt = cnt[0]
        return max(startCnt, endCnt, maxCnt // 2 if maxCnt % 2 == 0 else maxCnt // 2 + 1)


s = Solution()
data = [([1, 0, 0, 0, 1, 0, 1], 2),
        ([1, 0, 0, 0], 3),
        ([0, 0, 0, 1], 3),
        ([0, 1], 1),
        ([0, 1, 0, 0], 2),
        ([0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0], 9),
        ([0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1], 3),
        ]
for seats, expected in data:
    real = s.maxDistToClosest(seats)
    print('{}, expected {}, real {}, result {}'.format(seats, expected, real, expected == real))
