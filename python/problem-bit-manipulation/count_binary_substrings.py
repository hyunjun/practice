#   https://leetcode.com/problems/count-binary-substrings

#   https://leetcode.com/problems/count-binary-substrings/solution


class Solution:
    #   5.52%
    def countBinarySubstrings(self, s):
        if s is None or 0 == len(s):
            return 0
        prev, d, count = '', {'0': 0, '1': 0}, 0
        for n in s:
            if prev != n:
                prev = n
                d[n] = 1
            else:
                d[n] += 1
            if 0 < d['0'] and 0 < d['1']:
                count += 1
            if '0' == n:
                d['1'] -= 1
            else:
                d['0'] -= 1
        return count


solution = Solution()
data = [('00110011', 6),
        ('10101', 4),
        ('00100', 2),
        ('000', 0),
        ('111', 0),
        ]
for s, expected in data:
    real = solution.countBinarySubstrings(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
