#   https://leetcode.com/problems/coin-change
import sys


class Solution:
    def recur3(self, lastCoinNum, amount, num):
        #print(f'\n{self.coins}, {amount}, {num}')
        for i, c in enumerate(self.coins):
            if i < lastCoinNum or amount < c:
                continue
            elif amount == c:
                print('matched {}'.format(num + 1))
                if self.result == -1:
                    self.result = num + 1
                else:
                    self.result = min(num + 1, self.result)
            else:
                if self.result == -1 or num < self.result - 1:
                    #print(f'{amount - c}')
                    self.recur3(i, amount - c, num + 1)

    def recur2(self, coins, amount, num):
        #print(f'\n{coins}, {amount}, {num}')
        for i, c in enumerate(coins):
            if amount < c:
                continue
            elif amount == c:
                print('matched {}'.format(num + 1))
                if self.result == -1:
                    self.result = num + 1
                else:
                    self.result = min(num + 1, self.result)
            else:
                if self.result == -1 or num < self.result - 1:
                    self.recur2(coins[i:], amount - c, num + 1)

    def recur1(self, coins, amount, accNum, num):
        #print(f'\n{coins}, {amount}, {num}')
        for i, c in enumerate(coins):
            if amount < c:
                continue
            elif amount == c:
                print('matched {}'.format(num + 1))
                if self.result == -1:
                    self.result = num + 1
                else:
                    self.result = min(num + 1, self.result)
            else:
                if self.result == -1 or accNum < self.result - 1:
                    self.recur1(coins[i:], amount - c, accNum + 1, num + 1)

    def recur0(self, coins, amount, acc, num):
        #print(f'\n{coins}, {amount}, {acc}, {num}')
        for i, c in enumerate(coins):
            if amount < c:
                continue
            elif amount == c:
                print('matched {}, {}'.format(num + 1, acc + [c]))
                if self.result == -1:
                    self.result = num + 1
                else:
                    self.result = min(num + 1, self.result)
            else:
                if self.result == -1 or len(acc) < self.result - 1:
                    #print(f'recur {acc}, {self.result}')
                    self.recur0(coins[i:], amount - c, acc + [c], num + 1)

    def coinChangeRecur(self, coins, amount):
        if coins is None or 0 == len(coins) or 0 == amount:
            return 0

        coins.sort(reverse=True)
        self.result = -1
        #self.coins = coins
        #self.recur3(0, amount, 0)
        #self.recur2(coins, amount, 0)
        #self.recur1(coins, amount, 0, 0)
        #self.recur0(coins, amount, [], 0)
        return self.result

    def coinChangeInter(self, coins, amount):
        if coins is None or 0 == len(coins) or 0 == amount:
            return 0

        coins.sort(reverse=True)
        result = -1
        stack = [(coins, amount, 0)]
        while stack:
            coins, amount, num = stack.pop()
            for i, c in enumerate(coins):
                if amount < c:
                    continue
                elif amount == c:
                    #print(f'matched {num + 1}')
                    if result == -1:
                        result = num + 1
                    else:
                        result = min(num + 1, result)
                else:
                    if result == -1 or num < result - 1:
                        stack.append((coins[i:], amount - c, num + 1))
        return result

    #   solution #2 from https://leetcode.com/problems/coin-change/solution/
    #   maximum recursion error
    def coinChangeRe(self, coins, rem, count):
        if rem < 0:
            return -1
        if 0 == rem:
            return 0
        if count[rem - 1] != 0:
            return count[rem - 1]
        _min = sys.maxsize
        for c in coins:
            res = self.coinChangeRe(coins, rem - c, count)
            if 0 <= res < _min:
                _min = 1 + res
        if _min == sys.maxsize:
            count[rem - 1] =  -1
        else:
            count[rem - 1] =  _min
        return count[rem - 1]

    def coinChangeSol2(self, coins, amount):
        if amount < 1:
            return 0
        return self.coinChangeRe(coins, amount, [0] * amount)

    #   solution #3 from  https://leetcode.com/problems/coin-change/solution
    #   위의 recursive solution의 대략 2배 속도
    def coinChange0(self, coins, amount):
        _max = amount + 1
        dp = [_max] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        if amount < dp[amount]:
            return -1
        return dp[amount]

    #   17.63%
    def coinChange(self, coins, amount):
        if amount <= 0:
            return 0
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for coin in coins:
                if i < coin:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        if amount < dp[-1]:
            return -1
        return dp[-1]



s = Solution()
data = [([1, 2, 5], 11, 3), ([1, 2, 5], 13, 4), ([2], 3, -1), ([1], 0, 0),
        ([186, 419, 83, 408], 6249, 20), ([470, 35, 120, 81, 121], 9825, 30),
        ([3, 7, 405, 436], 8839, 25), ([190, 80, 457, 111, 240], 6159, 17),
        ([271, 5, 343, 254, 112], 4853, 17), ([265, 398, 46, 78, 52], 7754, 25),
        ([235, 326, 180, 11, 61, 483, 464, 125, 403, 241], 5926, 14)
        ]
for coins, amount, expected in data:
    real = s.coinChange(coins, amount)
    print('coins {}, amount {}\texpected {} real {} result {}'.format(coins, amount, expected, real, expected == real))
