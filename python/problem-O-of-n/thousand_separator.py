#   https://leetcode.com/problems/thousand-separator


class Solution:
    #   runtime; 28ms, 88.68%
    #   memory; 13.8MB, 69.37%
    def thousandSeparator(self, n: int) -> str:
        strN, res = str(n), []
        i = len(strN) - 1
        while 0 <= i:
            if 0 <= i - 2:
                res.insert(0, '.' + strN[i - 2:i + 1])
                i -= 3
            else:
                while 0 <= i:
                    res.insert(0, strN[i])
                    i -= 1
        ret = ''.join(res)
        if ret[0] == '.':
            return ret[1:]
        return ret


s = Solution()
data = [(987, '987'),
        (1234, '1.234'),
        (123456789, '123.456.789'),
        (0, '0'),
        ]
for n, expect in data:
    real = s.thousandSeparator(n)
    print(f'{n} expect {expect} real {real} result {expect == real}')
