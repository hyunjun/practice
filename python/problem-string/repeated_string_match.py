#   https://leetcode.com/problems/repeated-string-match

#   https://leetcode.com/problems/repeated-string-match/solution


class Solution:
    #   Wrong Answer
    def repeatedStringMatch0(self, A, B):
        if A is None or 0 == len(A) or B is None or 0 == len(B):
            return -1
        cnt = 1
        while True:
            if len(A * cnt) == len(B):
                if B in A * cnt:
                    return cnt
            elif len(A * cnt) > len(B):
                if B in A * cnt:
                    return cnt
                return -1
            cnt += 1
        return -1

    #   82.63%
    def repeatedStringMatch0(self, A, B):
        if A is None or 0 == len(A) or B is None or 0 == len(B):
            return -1
        def match(s):
            #print(s)
            if 0 < len(s):
                if A == s or s in A:
                    return 1
                elif A in s:
                    l = s.index(A)
                    r = l + len(A)
                    if (l - 1 < 0 or 0 <= l - 1 and s[l - 1] == A[-1]) and (len(s) <= r or r < len(s) and s[r] == A[0]):
                        tmp = match(s[:l] + s[r:])
                        if -1 != tmp:
                            return 1 + tmp
                elif s in A * 2:
                    return 2
                return -1
            return 0
        return match(B)

    #   18.04%
    def repeatedStringMatch(self, A, B):
        if A == B or B in A:
            return 1
        a, cnt = A, 0
        while len(a) <= len(B):
            cnt += 1
            a = A * cnt
            #print('{} {} {}'.format(a, B, a in B))
            if B in a:
                return cnt
        if B in A * (cnt + 1):
            return cnt + 1
        if B in A * (cnt + 2):
            return cnt + 2
        return -1


s = Solution()
data = [('abcd', 'cdabcdab', 3),
        ('a', 'aa', 2),
        ('aa', 'a', 1),
        ('abc', 'cabcabca', 4),
        ('abc', 'ca', 2),
        ('abcabcabcabc', 'abac', -1),
        ('abcd', 'abcdb', -1),
        ('abccb', 'cbabccb', 2),
        ('abcd', 'cdabcdacdabcda', -1),
        ]
for A, B, expected in data:
    real = s.repeatedStringMatch0(A, B)
    real2 = s.repeatedStringMatch(A, B)
    print('{}, {}, expected {}, real {}, real2 {}, result {}'.format(A, B, expected, real, real2, expected == real == real2))

