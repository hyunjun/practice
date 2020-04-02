#   https://leetcode.com/problems/count-number-of-teams


from typing import List


class Solution:
    #   runtime; 2268ms, 13.01%
    #   memory; 13.8MB, 100.00%
    def numTeams(self, rating: List[int]) -> int:
        if rating is None or not (1 <= len(rating) <= 10 ** 5):
            return 0

        self.cnt = 0

        '''
        def accBigger(acc, s):
            if len(acc) == 3:
                self.cnt += 1
                return
            for i in range(s, len(rating)):
                if 0 == len(acc) or acc[-1] < rating[i]:
                    acc.append(rating[i])
                    accBigger(acc, i + 1)
                    acc.pop()

        #accBigger([], 0)

        def accSmaller(acc, s):
            if len(acc) == 3:
                self.cnt += 1
                return
            for i in range(s, len(rating)):
                if 0 == len(acc) or acc[-1] > rating[i]:
                    acc.append(rating[i])
                    accSmaller(acc, i + 1)
                    acc.pop()

        #accSmaller([], 0)
        '''

        def accFunc(acc, s, op):
            if len(acc) == 3:
                self.cnt += 1
                return
            for i in range(s, len(rating)):
                if 0 == len(acc) or op(acc[-1], rating[i]):
                    acc.append(rating[i])
                    accFunc(acc, i + 1, op)
                    acc.pop()

        accFunc([], 0, lambda a, b: a < b)
        accFunc([], 0, lambda a, b: a > b)

        return self.cnt


s = Solution()
data = [([2, 5, 3, 4, 1], 3),
        ([2, 1, 3], 0),
        ([1, 2, 3, 4], 4),
        ]
for rating, expected in data:
    real = s.numTeams(rating)
    print(f'{rating} expected {expected} real {real} result {expected == real}')
