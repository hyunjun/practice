#   https://leetcode.com/problems/ugly-number-ii


class Solution:

    #   6.98%
    def nthUglyNumber0(self, n):
        uglyNumber = 1
        if 1 == n:
            return uglyNumber
        uglies = [2, 3, 5]
        for i in range(2, n + 1):
            uglyNumber = uglies[0]
            del uglies[0]
            #print('[{}], {}, {}'.format(i, uglyNumber, uglies))
            for d in [2, 3, 5]:
                if uglyNumber * d not in uglies:
                    uglies.append(uglyNumber * d)
            uglies.sort()
        return uglyNumber

    #   48.06%
    def nthUglyNumber(self, n):
        uglyNumber = 1
        if 1 == n:
            return uglyNumber
        q2, q3, q5 = [2], [3], [5]
        for i in range(2, n + 1):
            uglyNumber = min(q2[0], q3[0], q5[0])
            if uglyNumber == q2[0]:
                del q2[0]
            if uglyNumber == q3[0]:
                del q3[0]
            if uglyNumber == q5[0]:
                del q5[0]
            q2.append(uglyNumber * 2)
            q3.append(uglyNumber * 3)
            q5.append(uglyNumber * 5)
        return uglyNumber


s = Solution()
data = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 8), (8, 9), (9, 10), (10, 12), (1690, 2123366400)]
for n, expected in data:
    real = s.nthUglyNumber(n)
    print('{}, expected {}, real {}, result {}'.format(n, expected, real, expected == real))
'''
    2 3 5
1   0 0 0
2   1 0 0
3   0 1 0
4   2 0 0
5   0 0 1
6   1 1 0
7   3 0 0
8   0 2 0
9   1 0 1
10  2 1 0
11  0 1 1   15
12  4 0 0   16
13  1 2 0   18
'''
