#   https://leetcode.com/problems/nim-game

#   https://leetcode.com/problems/nim-game/solution


class Solution:
    #   Wrong Answer
    def canWinNim0(self, n):
        if n <= 0:
            return False
        queue, result = [(n, True)], []
        while queue:
            stones, myTurn = queue[0]
            del queue[0]
            if stones in [1, 2, 3]:
                result.append(myTurn)
                continue
            for i in [3, 2, 1]:
                if 0 < stones - i:
                    queue.append((stones - i, not myTurn))
        return any([r == True for r in result])

    #   Memory Error
    def canWinNim1(self, n):
        if n <= 0:
            return False
        result = [None] * n
        result[0] = True
        for idx in range(n - 3):
            for i in range(1, 4):
                if result[idx + i]:
                    result[idx + i] = (not result[idx]) and result[idx + i]
                else:
                    result[idx + i] = not result[idx]
            print(result)
        return result[-1]

    #   Time Limit Exceeded
    def canWinNim2(self, n):
        if n <= 0:
            return False
        result = {0: True}
        for idx in range(n - 3):
            for i in range(1, 4):
                if idx + i in result:
                    result[idx + i] = (not result[idx]) and result[idx + i]
                else:
                    result[idx + i] = not result[idx]
            del result[idx]
        return result[n - 1]

    #   Time Limit Exceeded
    def canWinNim3(self, n):
        if n <= 0 or 4 == n:
            return False
        if n in [1, 2, 3]:
            return True
        turn, result = False, [(n - 1, False), (n - 2, False), (n - 3, False)]
        while 1 < result[2][0]:
            turn = not turn
            num = result[0][0]
            result[0] = (num - 1, result[1][1] and turn)
            result[1] = (num - 2, result[0][1] and turn)
            result[2] = (num - 3, turn)
            print(turn, result)
        return result[2][1]

    #   Wrong Answer
    def canWinNim(self, n):
        if n <= 0 or 4 == n:
            return False
        if n in [1, 2, 3, 5, 6]:
            return True
        turn, result = False, [(n - 1, False), (n - 2, False), (n - 3, False), (n - 4, None), (n - 5, None)]
        while 1 < result[4][0] or result[4][1] is None:
            turn = not turn
            for i in range(5):
                result[i] = (result[i][0] - 1, turn)
            print(turn, result)
        return result[4][1]

    def canWinNim(self, n):
        return n % 4 != 0


s = Solution()
data = [(4, False), (7, True),  (10, True), (13, True),  (16, False),
        (5, True),  (8, False), (11, True),  (14, True), (17, True),
        (6, True),  (9, True),  (12, False), (15, True), (18, True),
        (1348820612, False)
        ]
for n, expected in data:
    real = s.canWinNim(n)
    print('{}, expected {}, real {}, result {}'.format(n, expected, real, expected == real))
'''
4 3 2 1
T F F F
t 5 4 3 2 1
T T T T
F   F F F
T     T T T
t 6 5 4 3 2 1
T T T T
F   F F F
T     T T T T
t 7 6 5 4 3 2 1
T T
F   F F F
T     T T T T T
t 8 7 6 5 4 3 2 1
T T
F   F F F
T     T T T T T
F       F F F F F
t 9 8 7 6 5 4 3 2 1
T T
F   F F F
T     T T T T T
F       F F F F F
T         T T T T T
t 10 9 8 7 6 5 4 3 2 1
T T
F    F F F
T      F F T T T
F        F F F F F
T          T T T T T
'''
