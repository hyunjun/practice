#   https://leetcode.com/problems/convert-to-base-2

#   https://leetcode.com/problems/convert-to-base-2/discuss/265688/4-line-python-clear-solution-with-explanation


class Solution:
    #   Runtime Error
    def baseNeg20(self, N):
        if 0 == N:
            return '0'
        if 1 == N:
            return '1'

        def getLowerBound(bit):
            n, b = 0, bit - 1
            while b > 0:
                n += 2 ** b
                b -= 2
            return n
        def getUpperBound(bit):
            n, b = 0, bit - 2
            while b >= 0:
                n += 2 ** b
                b -= 2
            return n
        bitIdx = 0
        while not (2 ** bitIdx - getLowerBound(bitIdx) <= N <= 2 ** bitIdx + getUpperBound(bitIdx)):
            bitIdx += 2
        ret = [0] * (bitIdx + 1)
        ret[bitIdx] = 1
        if N % 2 != 0:
            ret[0] = 1
        num = 2 ** bitIdx + ret[0]
        diff, negBitIdx = num - N, 1
        while 2 ** negBitIdx <= diff:
            negBitIdx += 2
        negBitIdx -= 2
        while 0 < diff:
            if 2 ** negBitIdx <= diff:
                diff -= 2 ** negBitIdx
                ret[negBitIdx] = 1
            negBitIdx -= 2
        return ''.join([str(d) for d in ret[::-1]])

    #   Wrong Answer
    def baseNeg21(self, N):
        if 0 == N:
            return '0'
        if 1 == N:
            return '1'

        def getLowerBound(bit):
            n, b = 0, bit - 1
            while b > 0:
                n += 2 ** b
                b -= 2
            return n
        def getUpperBound(bit):
            n, b = 0, bit - 2
            while b >= 0:
                n += 2 ** b
                b -= 2
            return n
        bitIdx = 0
        while not (2 ** bitIdx - getLowerBound(bitIdx) <= N <= 2 ** bitIdx + getUpperBound(bitIdx)):
            bitIdx += 2
        isOdd = False
        if N % 2 == 1:
            N -= 1
            isOdd = True
        isPosBit, num = False, 2 ** bitIdx
        ret = ['1']
        bitIdx -= 1
        while 0 <= bitIdx:
            if num == N:
                [ret.append('0') for _ in range(bitIdx + 1)]
                break
            else:
                if isPosBit:
                    if N - num >= 2 ** (bitIdx - 1):
                        ret.append('1')
                        num += 2 ** bitIdx
                    else:
                        ret.append('0')
                else:
                    if num - N >= 2 ** (bitIdx - 1):
                        ret.append('1')
                        num -= 2 ** bitIdx
                    else:
                        ret.append('0')
                isPosBit = not isPosBit
                bitIdx -= 1
        if isOdd:
            ret[-1] = '1'
        return ''.join(ret)

    #   runtime; 36ms, 100.00%
    #   memory; 13.1MB, 100.00%
    def baseNeg2(self, N):
        if 0 == N:
            return '0'
        if 1 == N:
            return '1'

        isOdd = False
        if N % 2 == 1:
            isOdd = True
            N -= 1

        bit = 0
        while 2 ** bit <= N:
            bit += 1
        bit -= 1
        ret = [0] * (bit + 1)
        while 0 <= bit:
            if 0 < N:
                if 2 ** bit <= N:
                    ret[bit] = 1
                    N -= 2 ** bit
            bit -= 1

        i = 1
        while i < len(ret):
            if ret[i] >= 2:
                ret[i] -= 2
                if i + 1 == len(ret):
                    ret.append(1)
                else:
                    ret[i + 1] += 1
            if ret[i] == 1 & i % 2 == 1:
                if i + 1 == len(ret):
                    ret.append(1)
                else:
                    ret[i + 1] += 1
            i += 1

        if isOdd:
            ret[0] = 1
        return ''.join([str(r) for r in ret[::-1]])


s = Solution()
data = [(0, '0'),
        (1, '1'),
        (2, '110'),
        (3, '111'),
        (4, '100'),
        (5, '101'),
        (6, '11010'),
        (7, '11011'),
        (8, '11000'),
        (9, '11001'),
        (10, '11110'),
        (11, '11111'),
        (12, '11100'),
        (13, '11101'),
        (14, '10010'),
        (15, '10011'),
        (16, '10000'),
        (38, '1111010'),
        ]
for N, expected in data:
    real = s.baseNeg2(N)
    print('{}, expected {}, real {}, result {}'.format(N, expected, real, expected == real))
