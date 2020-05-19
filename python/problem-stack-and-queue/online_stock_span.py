#   https://leetcode.com/problems/online-stock-span

#   https://leetcode.com/problems/online-stock-span/solution

#   https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3334


#   runtime; 952ms
#   memory; 18.4MB
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if 0 == len(self.stack):
            self.stack.append((price, 1))
        else:
            lessCnt = 0
            while 0 < len(self.stack) and self.stack[-1][0] <= price:
                _, cnt = self.stack.pop()
                lessCnt += cnt
            self.stack.append((price, lessCnt + 1))
        return self.stack[-1][1]
        

obj = StockSpanner()
data = [([100, 80, 60, 70, 60, 75, 85], [1, 1, 1, 2, 1, 4, 6]),
        ([31, 41, 48, 59, 79], [1, 2, 3, 4, 5]),
        ]
for prices, expected in data:
    real = [obj.next(price) for price in prices]
    print(f'{prices} expected {expected} real {real} result {expected == real}')
