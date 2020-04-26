#   https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k


class Solution:
    #   Time Limit Exceeded
    def findMinFibonacciNumbers0(self, k: int) -> int:
        if not (1 <= k <= 10 ** 9):
            return 0
        fibs = [1, 1]
        while fibs[-1] < k:
            fibs.append(fibs[-1] + fibs[-2])

        self.res = float('inf')
        def getSum(acc, cnt, fibs):
            if acc == k:
                self.res = min(self.res, cnt)
            elif acc < k:
                for i, f in enumerate(fibs):
                    if acc + f <= k and cnt + 1 <= self.res:
                        getSum(acc + f, cnt + 1, fibs[:i] + fibs[i + 1:])

        getSum(0, 0, fibs[::-1])

        return self.res

    #   runtime; 64ms, 29.18%
    #   memory; 13.7MB, 100.00%
    def findMinFibonacciNumbers(self, k: int) -> int:
        if not (1 <= k <= 10 ** 9):
            return 0
        fibs = [1, 1]
        while fibs[-1] < k:
            fibs.append(fibs[-1] + fibs[-2])

        curSum, cnt = 0, 0
        for f in fibs[::-1]:
            if curSum + f <= k:
                curSum += f
                cnt += 1
                if curSum == k:
                    break

        return cnt


s = Solution()
data = [(7, 2),
        (10, 2),
        (19, 3),
        (513314, 0),
        ]
for k, expected in data:
    real = s.findMinFibonacciNumbers(k)
    print(f'{k} expected {expected} real {real} result {expected == real}')
