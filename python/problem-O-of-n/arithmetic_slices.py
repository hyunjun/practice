#   https://leetcode.com/problems/arithmetic-slices

#   https://leetcode.com/problems/arithmetic-slices/solution


class Solution:
    #   3.76%
    def numberOfArithmeticSlices0(self, A):
        def getTotalCount(num):
            _sum, cnt = 0, 1
            for i in range(num, 2, -1):
                _sum += cnt
                cnt += 1
            return _sum

        if A is None or len(A) < 3:
            return 0
        diff, prev, res = A[1] - A[0], 0, 0
        for i in range(1, len(A)):
            if diff != A[i] - A[i - 1]:
                res += getTotalCount(i - prev)
                diff = A[i] - A[i - 1]
                prev = i - 1
        res += getTotalCount(len(A) - prev)
        return res

    #   https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3644
    #   runtime; 44ms, 22.84%
    #   memory; 14.6MB, 17.20%
    def numberOfArithmeticSlices(self, A):
        if A is None or len(A) < 3:
            return 0

        def getCount(n):
            if n >= 3:
                return (n - 2) * (n - 1) // 2
            return 0

        s, diff, cnt = 0, A[1] - A[0], 0
        for i, a in enumerate(A):
            if 0 == i:
                continue
            if a - A[i - 1] != diff:
                cnt += getCount(i - s)
                print(s, i - 1)
                diff, s = a - A[i - 1], i - 1
        cnt += getCount(len(A) - s)
        print(s, len(A) - 1)
        return cnt


s = Solution()
data = [([1, 3, 5, 7, 9], 6),
        ([1, 2, 3, 4], 3),
        ([1, 2, 3, 5, 7], 2),
        ]
for A, expect in data:
    real = s.numberOfArithmeticSlices(A)
    print(f'{A}, expect {expect}, real {real}, result {expect == real}')
'''
1 2 3 = 1
1 2 3 4 = 1 2 3, 2 3 4 = 2
1 2 3 4 5 = 1 2 3 4, 2 3 4 5 = 1 2 3, 2 3 4, 2 3 4, 3 4 5 = 6
1 2 3 4 5 6 = 1 2 3 4 5, 2 3 4 5 6 = 1 2 3 4, 2 3 4 5, 3 4 5 6 = 1 2 3, 2 3 4, 3 4 5, 4 5 6 = 1 + 2 + 3 + 4 = 10
'''
