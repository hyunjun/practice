#   https://leetcode.com/problems/car-pooling

#   https://leetcode.com/problems/car-pooling/solution


from collections import defaultdict
from typing import List


class Solution:
    #   https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3467
    #   runtime; 400ms, 5.09%
    #   memory; 14.3MB, 54.07%
    def carPooling0(self, trips: List[List[int]], capacity: int) -> bool:
        d = defaultdict(int)
        for trip in trips:
            passenger, start, end = trip
            for i in range(start, end):
                d[i] += passenger
                if d[i] > capacity:
                    return False
        return True

    #   runtime; 64ms, 76.39%
    #   memory; 14.2MB, 73.66%
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d, maxDst = defaultdict(int), 0
        for trip in trips:
            d[trip[1]] += trip[0]
            d[trip[2]] -= trip[0]
            maxDst = max(maxDst, trip[2])
        curCapacity = 0
        for i in range(maxDst + 1):
            curCapacity += d[i]
            if curCapacity > capacity:
                return False
        return True


s = Solution()
data = [([[2,1,5],[3,3,7]], 4, False),
        ([[2,1,5],[3,3,7]], 5, True),
        ([[2,1,5],[3,5,7]], 3, True),
        ([[3,2,7],[3,7,9],[8,3,9]], 11, True),
        ]
for trips, capacity, expect in data:
    real = s.carPooling(trips, capacity)
    print(f'{trips} {capacity} expect {expect} real {real} result {expect == real}')
