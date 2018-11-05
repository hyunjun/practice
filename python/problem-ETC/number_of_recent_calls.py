#   https://leetcode.com/problems/number-of-recent-calls


class RecentCounter:
    def __init__(self):
        self.min, self.q = None, []

    #   680ms, 100.00%
    def ping(self, t):
        self.min = t - 3000
        while 0 < len(self.q) and self.q[0] < self.min:
            self.q.pop(0)
        self.q.append(t)
        return len(self.q)


r = RecentCounter()
data = [(1, 1),    # -2999, 1
        (100, 2),  # -2900, 1, 100
        (3001, 3), # 1, 100, 3001
        (3002, 3), # 2, 100, 3001, 3002
        ]
for t, expected in data:
    real = r.ping(t)
    print('{}, expected {}, real {}, result {}'.format(t, expected, real, expected == real))
