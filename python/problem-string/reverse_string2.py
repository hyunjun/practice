#   https://leetcode.com/problems/reverse-string-ii

#   https://leetcode.com/problems/reverse-string-ii/solution


class Solution:
    #   34.35%
    def reverseStr(self, s, k):
        if s is None or 0 == len(s):
            return s
        if k < 1:
            return None

        l = list(s)
        lenL = len(l)
        for i in range(0, lenL, 2 * k):
            if lenL - i < k:
                s, e = i, lenL - 1
            else:
                s, e = i, i + k - 1
            while s < e:
                l[s], l[e] = l[e], l[s]
                s += 1
                e -= 1
        return ''.join(l)


solution = Solution()
data = [('abcdefg', 2, 'bacdfeg'),
        ('abcdefgh', 3, 'cbadefhg'),
        ]
for s, k, expected in data:
    real = solution.reverseStr(s, k)
    print('{}, {}, expected {}, real {}, result {}'.format(s, k, expected, real, expected == real))
