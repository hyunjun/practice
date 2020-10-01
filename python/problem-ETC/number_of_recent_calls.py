#   https://leetcode.com/problems/number-of-recent-calls

#   https://leetcode.com/problems/number-of-recent-calls/solution


#   runtime; 680ms, 100.00%
class RecentCounter0:
    def __init__(self):
        self.min, self.q = None, []

    def ping(self, t):
        self.min = t - 3000
        while 0 < len(self.q) and self.q[0] < self.min:
            self.q.pop(0)
        self.q.append(t)
        return len(self.q)

#   https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3480
#   runtime; 464ms, 25.99%
#   memory; 18.8MB, 15.02%
class RecentCounter:
    def __init__(self):
        self.start, self.pinged = float('-inf'), []

    def ping(self, t: int) -> int:
        self.start = 0 if t - 3000 < 0 else t - 3000
        self.pinged.append(t)
        self.pinged.sort()
        while 0 < len(self.pinged) and self.pinged[0] < self.start:
            self.pinged.pop(0)
        return len(self.pinged)


r = RecentCounter()
data = [(1, 1),    # -2999, 1
        (100, 2),  # -2900, 1, 100
        (3001, 3), # 1, 100, 3001
        (3002, 3), # 2, 100, 3001, 3002
        ]
for t, expect in data:
    real = r.ping(t)
    print(f'{t}, expect {expect}, real {real}, result {expect == real}')
