# https://leetcode.com/problems/add-binary


class Solution:
    def add_binary(a, b):
        if (a is None or 0 == len(a)) and (b is None or 0 == len(b)):
            return '0'
        if a is None or 0 == len(a) or '0' == a:
            return b
        if b is None or 0 == len(b) or '0' == b:
            return a
    
        result, longer, shorter = [], a[::-1], b[::-1]
        if len(a) < len(b):
            longer, shorter = shorter, longer
    
        transfer = 0
        #print('shorter {}\tlonger {}'.format(shorter, longer))
        for i, c in enumerate(shorter):
            l = [int(c), int(longer[i]), transfer]
            l.sort()
            #print('[{}]\t{}'.format(i, l))
            if l == [0, 0, 0]:
                result.append(0)
                transfer = 0
            elif l == [0, 0, 1]:
                result.append(1)
                transfer = 0
            elif l == [0, 1, 1]:
                result.append(0)
                transfer = 1
            else:
                result.append(1)
                transfer = 1
        #print('[after 1st loop]\tresult {}\ttransfer {}'.format(result, transfer))
        if len(shorter) < len(longer):
            #print('loop from {} to {}'.format(len(shorter), len(longer)))
            for i in range(len(shorter), len(longer)):
                l = [int(longer[i]), transfer]
                l.sort()
                #print('[{}]\t{}'.format(i, l))
                if l == [0, 0]:
                    result.append(0)
                    transfer = 0
                elif l == [1, 1]:
                    result.append(0)
                    transfer = 1
                else:
                    result.append(1)
                    transfer = 0
        if transfer == 1:
            result.append(1)
        #print('[after 2nd loop]\tresult {}\ttransfer {}'.format([c for c in result[::-1]], transfer))
        return str(''.join([str(c) for c in result[::-1]]))

    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3395
    #   runtime; 24ms, 97.57%
    #   memory; 13.6MB, 95.27%
    def addBinary0(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    #   runtime; 44ms, 31.30%
    #   memory; 13.9MB, 46.03%
    def addBinary1(self, a: str, b: str) -> str:
        l, s = b, a
        if len(a) > len(b):
            l, s = a, b
        carry, l, s, res = '0', l[::-1], s[::-1], []
        for i in range(len(s)):
            nums = sorted([l[i], s[i], carry])
            if nums == ['0', '0', '0']:
                carry = '0'
                res.append('0')
            elif nums == ['0', '0', '1']:
                carry = '0'
                res.append('1')
            elif nums == ['0', '1', '1']:
                carry = '1'
                res.append('0')
            else:
                carry = '1'
                res.append('1')
        for i in range(len(s), len(l)):
            nums = sorted([l[i], carry])
            if nums == ['0', '0']:
                carry = '0'
                res.append('0')
            elif nums == ['0', '1']:
                carry = '0'
                res.append('1')
            else:
                carry = '1'
                res.append('0')
        if carry == '1':
            res.append('1')
        return ''.join(res[::-1])

    #   runtime; 36ms, 59.78%
    #   memory; 13.9MB, 25.97%
    def addBinary2(self, a: str, b: str) -> str:
        l, s = b, a
        if len(a) > len(b):
            l, s = a, b
        s = '0' * (len(l) - len(s)) + s
        carry, l, s, res = '0', l[::-1], s[::-1], []
        for i in range(len(l)):
            nums = sorted([l[i], s[i], carry])
            if nums == ['0', '0', '0']:
                carry = '0'
                res.append('0')
            elif nums == ['0', '0', '1']:
                carry = '0'
                res.append('1')
            elif nums == ['0', '1', '1']:
                carry = '1'
                res.append('0')
            else:
                carry = '1'
                res.append('1')
        if carry == '1':
            res.append('1')
        return ''.join(res[::-1])

    #   runtime; 44ms, 31.30%
    #   memory; 13.9MB, 46.03%
    def addBinary(self, a: str, b: str) -> str:
        l, s = b, a
        if len(a) > len(b):
            l, s = a, b
        s = '0' * (len(l) - len(s)) + s
        carry, res = '0', []
        for i in range(len(l) - 1, -1, -1):
            nums = sorted([l[i], s[i], carry])
            if nums == ['0', '0', '0']:
                carry = '0'
                res.append('0')
            elif nums == ['0', '0', '1']:
                carry = '0'
                res.append('1')
            elif nums == ['0', '1', '1']:
                carry = '1'
                res.append('0')
            else:
                carry = '1'
                res.append('1')
        if carry == '1':
            res.append('1')
        return ''.join(res[::-1])


s = Solution()
cases = [('11', '1', '100'),
         ('0', '0', '0'),
         ('1', '1', '10'),
         ('111', '1', '1000'),
         ('1010', '1011', '10101'),
         ('100', '110010', '110110'),
         ('11', '1', '100'),
         ]
for a, b, expect in cases:
    real = s.addBinary(a, b)
    print(f'{a} {b} expect {expect} real {real} result {expect == real}')
