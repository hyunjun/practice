#   https://leetcode.com/problems/beautiful-arrangement

#   https://leetcode.com/problems/beautiful-arrangement/solution


class Solution:
    d = {1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
         2: [1, 2, 4, 6, 8, 10, 12, 14], 3: [1, 3, 6, 9, 12, 15],
         4: [1, 2, 4, 8, 12], 5: [1, 5, 10, 15], 6: [1, 2, 3, 6, 12],
         7: [1, 7, 14], 8: [1, 2, 4, 8], 9: [1, 3, 9],
         10: [1, 2, 5, 10], 11: [1, 11], 12: [1, 2, 3, 4, 6, 12],
         13: [1, 13], 14: [1, 2, 7, 14], 15: [1, 3, 5, 15]}

    #   60.87%
    def countArrangement(self, N):
        if N <= 0 or 15 < N:
            return 0
        self.res = 0
        def cnt(usedSet, n):
            if n == N:
                for i in Solution.d[n]:
                    if i in usedSet:
                        continue
                    if N < i:
                        break
                    #print(usedSet, i)
                    self.res += 1
            else:
                for i in Solution.d[n]:
                    if i in usedSet:
                        continue
                    if N < i:
                        break
                    usedSet.add(i)
                    cnt(usedSet, n + 1)
                    usedSet.remove(i)
        cnt(set(), 1)
        return self.res


s = Solution()
data = [(2, 2),
        (3, 3),
        (15, 24679),
        ]
for N, expected in data:
    real = s.countArrangement(N)
    print('{}, expected {}, real {}, result {}'.format(N, expected, real, expected == real))
'''
i   num/i               i/num
1   ALL                 1
2   even                1, 2
3   3, 6, 9, 12, 15     1, 3
4   4, 8, 12            1, 2, 4
5   5, 10, 15           1, 5
6   6, 12               1, 2, 3, 6
7   7, 14               1, 7
8   8                   1, 2, 4, 8
9   9                   1, 3, 9
10  10                  1, 2, 5, 10
11  11                  1, 11
12  12                  1, 2, 3, 4, 6, 12
13  13                  1, 13
14  14                  1, 2, 7, 14
15  15                  1, 3, 5, 15
'''
