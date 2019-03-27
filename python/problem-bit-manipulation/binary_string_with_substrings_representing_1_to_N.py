#   https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n


class Solution:
    #   runtime; 36ms, 100.00%
    #   memory; 13.2MB, 100.00%
    def queryString(self, S, N):

        def int2bitStr(num):
            maxBit = 0
            while 2 ** maxBit <= num:
                maxBit += 1
            maxBit -= 1
            bitNum, res = 2 ** maxBit, []
            while 0 < bitNum:
                if bitNum <= num:
                    num -= bitNum
                    res.append('1')
                else:
                    res.append('0')
                bitNum //= 2
            return ''.join(res)

        v = set()
        for i in range(N, 0, -1):
            if i in v:
                continue
            num = i
            s = int2bitStr(num)
            idx = len(s)
            while 0 < idx:
                if num not in v:
                    if s[:idx] not in S:
                        return False
                    v.add(num)
                idx -= 1
                num >>= 1
        return True


s = Solution()
data = [('0110', 3, True),
        ('0110', 4, False),
        ]
for S, N, expected in data:
    real = s.queryString(S, N)
    print('{}, {}, expected {}, real {}, result {}'.format(S, N, expected, real, expected == real))
