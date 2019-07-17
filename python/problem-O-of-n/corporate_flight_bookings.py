#   https://leetcode.com/problems/corporate-flight-bookings

#   https://leetcode.com/problems/corporate-flight-bookings/discuss/331192/Easy-Python-O(n)-Let's-step-through-the-algorithm


from collections import defaultdict
from typing import List


class Solution:
    #   Time Limit Exceeded
    def corpFlightBookings0(self, bookings: List[List[int]], n: int) -> List[int]:
        if bookings is None or 0 == len(bookings):
            return []
        res = [0] * n
        for s, e, seats in bookings:
            for i in range(s - 1, e):
                res[i] += seats
        return res

    #   Time Limit Exceeded
    def corpFlightBookings1(self, bookings: List[List[int]], n: int) -> List[int]:
        if bookings is None or 0 == len(bookings):
            return []
        d = defaultdict(int)
        for s, e, seats in bookings:
            d[(s, e, seats)] += 1
        res = [0] * n
        for (s, e, seats), cnt in d.items():
            for i in range(s - 1, e):
                res[i] += seats * cnt
        return res

    #   runtime; 264ms, 69.64%
    #   memory; 23.1MB, 100.00%
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        if bookings is None or 0 == len(bookings):
            return []
        res = [0] * (n + 1)
        for s, e, seats in bookings:
            res[s - 1] += seats
            res[e] += -seats
        for i in range(1, len(res)):
            res[i] += res[i - 1]
        return res[:-1]


s = Solution()
data = [([[1,2,10],[2,3,20],[2,5,25]], 5, [10,55,45,25,25]),
        ]
for bookings, n, expected in data:
    real = s.corpFlightBookings(bookings, n)
    print(f'{bookings}, {n}, expected {expected}, real {real}, result {expected == real}')
