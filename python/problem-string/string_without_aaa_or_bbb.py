#   https://leetcode.com/problems/string-without-aaa-or-bbb

#   https://leetcode.com/problems/string-without-aaa-or-bbb/solution


class Solution:
    #   Wrong Answer
    def strWithout3a3b0(self, A, B):

        def getNAndNextNum(num):
            n = 2 if 2 < num else num
            num = num - 2 if 2 < num else 0
            return n, num

        a, b, flag, ret = A, B, False if A < B else True, []
        while 0 < a and 0 < b:
            if flag:
                n, a = getNAndNextNum(a)
                ret.append('a' * n)
            else:
                n, b = getNAndNextNum(b)
                ret.append('b' * n)
            flag = not flag
        while 0 < a:
            n, a = getNAndNextNum(a)
            ret.append('a' * n)
        while 0 < b:
            n, b = getNAndNextNum(b)
            ret.append('b' * n)
        return ''.join(ret)

    #   Wrong Answer
    def strWithout3a3b1(self, A, B):
        bigger, smaller = B if A < B else A, A if A < B else B
        bChar, sChar = 'b' if A < B else 'a', 'a' if A < B else 'b'
        ret = []
        while 0 < bigger:
            n = 2 if 2 < bigger else bigger
            ret.append(bChar * n)
            bigger -= n
        print(ret)
        retLen = len(ret)
        for i in range(retLen - 1, 0, -1):
            n = 2 if retLen < smaller else 1
            ret.insert(i, sChar * n)
            smaller -= n
        while 0 < smaller:
            ret.append(sChar)
            smaller -= 1
        return ''.join(ret)

    #   36ms, 67,95%
    def strWithout3a3b(self, A, B):
        bigger, smaller = B if A < B else A, A if A < B else B
        bChar, sChar = 'b' if A < B else 'a', 'a' if A < B else 'b'
        ret = []
        while 0 < bigger:
            n = 2 if 2 < bigger else bigger
            ret.append(bChar * n)
            bigger -= n
        retBiggerLen = len(ret)
        smaller2CharLen = smaller - retBiggerLen
        smaller1CharLen = smaller - smaller2CharLen
        print(ret, retBiggerLen, smaller2CharLen, smaller1CharLen)
        for i in range(retBiggerLen - 1, 0, -1):
            if 0 < smaller2CharLen:
                ret.insert(i, sChar * 2)
                smaller2CharLen -= 1
                smaller -= 2
            else:
                ret.insert(i, sChar)
                smaller -= 1
        while 0 < smaller:
            ret.append(sChar)
            smaller -= 1
        return ''.join(ret)


s = Solution()
data = [(1, 2, ['abb', 'bab', 'bba']),
        (4, 1, ['aabaa']),
        (2, 5, ['bbabbab']),
        (6, 6, ['abababababab', 'aabbaabbaabb']),
        (27, 33, ['bbabbabbabbabbababababababababababababababababababababababab']),
        ]
for A, B, expectedList in data:
    real = s.strWithout3a3b(A, B)
    print('{}, {}, expectedList {}, real {}, result {}'.format(A, B, expectedList, real, real in expectedList))
