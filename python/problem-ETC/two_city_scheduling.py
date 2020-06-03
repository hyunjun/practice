#   https://leetcode.com/problems/two-city-scheduling


from typing import List


class Solution:
    #   Wrong Answer
    def twoCitySchedCost0(self, costs: List[List[int]]) -> int:
        if costs is None or not (1 <= len(costs) <= 100):
            return 0
        costs, halfLen, tot, aCnt, bCnt = sorted(costs, key=lambda t: (-abs(t[0] - t[1]), min(t[0], t[1]))), len(costs) // 2, 0, 0, 0
        for a, b in costs:
            if a < b and aCnt < halfLen:
                tot += a
                aCnt += 1
            else:
                tot += b
                bCnt += 1
        return tot

    #   Time Limit Exceeded
    def twoCitySchedCost1(self, costs: List[List[int]]) -> int:
        if costs is None or not (1 <= len(costs) <= 100):
            return 0

        self.tot = float('inf')
        def consume(acc, remains, isATurn):
            if self.tot < acc:
                return
            if 0 == len(remains):
                self.tot = min(self.tot, acc)
                return
            for i, (a, b) in enumerate(remains):
                if isATurn:
                    consume(acc + a, remains[:i] + remains[i + 1:], not isATurn)
                else:
                    consume(acc + b, remains[:i] + remains[i + 1:], not isATurn)

        consume(0, costs, True)
        return self.tot

    #   https://leetcode.com/problems/two-city-scheduling/discuss/667781/Python-3-Lines-O(n-log-n)-with-sort-explained
    #   runtime; 40ms, 73.29%
    #   memory; 13.8MB
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        if costs is None or not (1 <= len(costs) <= 100):
            return 0
        first, diff = [a for a, _ in costs], [b - a for a, b in costs]
        return sum(first) + sum(sorted(diff)[:len(costs) // 2])


s = Solution()
data = [([[10,20],[30,200],[400,50],[30,20]], 110),
        ([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]], 1859),
        ([[70,311],[74,927],[732,711],[126,583],[857,118],[97,928],[975,843],[175,221],[284,929],[816,602],[689,863],[721,888]], 4723),
        ]
for costs, expected in data:
    real = s.twoCitySchedCost(costs)
    print(f'{costs} expected {expected} real {real} result {expected == real}')
'''
    10 30 400 30
20  A   A   B   B
200
50
20

10  30   400 30
20  200  50  20
-10 -170 350 10

400 30  10 30
50  200 20 20
B   A   A  B
sort by abs(diff) min(a, b)
'''
