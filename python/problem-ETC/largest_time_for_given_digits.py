#   https://leetcode.com/problems/largest-time-for-given-digits


from itertools import product


class Solution:
    #   Wrong Answer
    def largestTimeFromDigits0(self, A):
        d = {i: 0 for i in range(10)}
        for a in A:
            d[a] += 1

        res = []
        for i in range(2, -1, -1):
            if 0 < d[i]:
                res.append(i)
                d[i] -= 1
                break
        if 0 == len(res):
            return ''
        s = 9
        if 2 == res[0]:
            s = 3
        for i in range(s, -1, -1):
            if 0 < d[i]:
                res.append(i)
                d[i] -= 1
                break
        if len(res) < 2:
            return ''
        for i in range(5, -1, -1):
            if 0 < d[i]:
                res.append(i)
                d[i] -= 1
                break
        if len(res) < 3:
            return ''
        for i in range(9, -1, -1):
            if 0 < d[i]:
                res.append(i)
        return '{}{}:{}{}'.format(res[0], res[1], res[2], res[3])

    #   212ms, 100.00%
    def largestTimeFromDigits1(self, A):
        sortedA = sorted(A)
        for h in range(23, -1, -1):
            if h < 10:
                h0, h1 = 0, h
            else:
                h0, h1 = int(str(h)[0]), int(str(h)[1])
            for m in range(59, -1, -1):
                if m < 10:
                    m0, m1 = 0, m
                else:
                    m0, m1 = int(str(m)[0]), int(str(m)[1])
                if sorted([h0, h1, m0, m1]) == sortedA:
                    return '{}{}:{}{}'.format(h0, h1, m0, m1)
        return ''

    #   https://leetcode.com/explore/featured/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3445
    #   runtime; 100ms
    #   memory; 13.8MB, 74.68%
    def largestTimeFromDigits(self, A):
        sortedA, m0, m1 = sorted(A), range(5, -1, -1), range(9, -1, -1)
        
        def makeTime(h0, h1):
            for (((a, b), c), d) in product(product(product(h0, h1), m0), m1):
                if sorted([a, b, c, d]) == sortedA:
                    return f'{a}{b}:{c}{d}'
            return ''
        
        ret = makeTime([2], range(3, -1, -1))
        return ret if 0 < len(ret) else makeTime([1, 0], range(9, -1, -1))


s = Solution()
data = [([1, 2, 3, 4], '23:41'),
        ([5, 5, 5, 5], ''),
        ([2, 0, 6, 6], '06:26'),
        ]
for A, expected in data:
    real = s.largestTimeFromDigits(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
