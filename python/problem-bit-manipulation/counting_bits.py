#   https://leetcode.com/problems/counting-bits

#   https://leetcode.com/problems/counting-bits/discuss/159457/DP-Solution-Python-4-lines-(O(n)-space-and-time)


class Solution:
    #   43.24%
    def countBits0(self, num):
        if 0 == num:
            return [0]
        res = [0] * (num + 1)
        res[1], twos = 1, 2
        for i in range(2, num + 1):
            if twos == i:
                res[i] = 1
                twos <<= 1
            else:
                res[i] = 1 + res[i - twos // 2]
        return res

    #   35.70%
    def countBits(self, num):
        res, twos = [0] * (num + 1), 2
        for i in range(1, num + 1):
            if twos == i:
                res[i] = 1
                twos <<= 1
            else:
                res[i] = 1 + res[i - twos // 2]
        return res


s = Solution()
data = [(2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
        ]
for num, expected in data:
    real = s.countBits(num)
    print('{}, expected {}, real {}, result {}'.format(num, expected, real, expected == real))
