#   https://www.youtube.com/watch?v=tj_sBZw9nS0


#   https://leetcode.com/problems/regular-expression-matching/submissions
#   runtime; 288ms, 31.72%
#   memory; 13MB, 86.41%
class Solution:
    def shorten(self, p):
        shortened = list(p)
        for i, c in enumerate(shortened):
            if '*' == c:
                if 0 <= i - 3 and '*' == shortened[i - 2] and shortened[i - 3] == shortened[i - 1]:
                    shortened[i - 3] = shortened[i - 2] = ''
        return ''.join(shortened)

    def isMatch(self, s, p):
        return self.isMatchRecur(s, self.shorten(p))

    def isMatchRecur(self, s, p):
        if 0 == len(s):
            if 0 == len(p):
                return True
            if 1 < len(p) and '*' == p[1]:
                return self.isMatchRecur(s, p[2:])
            return False
    
        if 1 < len(p) and '*' == p[1]:
            ret = self.isMatchRecur(s, p[2:])
            if ret:
                return True
            if '.' == p[0]:
                ret = self.isMatchRecur(s[1:], p)
                if ret:
                    return True
                i, cnt = 0, 1
                while cnt < len(s) and s[i] == s[cnt]:
                    cnt += 1
                for i in range(cnt):
                    ret = self.isMatchRecur(s[i + 1:], p[2:])
                    if ret:
                        return True
            elif 'a' <= p[0] <= 'z':
                cnt = 0
                while cnt < len(s) and s[cnt] == p[0]:
                    cnt += 1
                for i in range(cnt):
                    ret = self.isMatchRecur(s[i + 1:], p[2:])
                    if ret:
                        return True
        if 0 < len(p) and '.' == p[0]:
            return self.isMatchRecur(s[1:], p[1:])
        if 0 < len(p) and 'a' <= p[0] <= 'z':
            if s[0] == p[0]:
                return self.isMatchRecur(s[1:], p[1:])
        return False


solution = Solution()
data = [('aba', 'ab', False),
        ('aa', 'a*', True),
        ('ab', '.*', True),
        ('ab', '.', False),
        ('aab', 'c*a*b', True),
        ('aaa', 'a*.', True),
        ("mississippi", "mis*is*p*.", False),
        ('a', '.*..a*', False),
        ("bbbaabbccbcccccccac", "bba*.*.*c*.*c*b*a", False),
        ]
for s, p, expected in data:
    real = solution.isMatch(s, p)
    print(f'{s}, {p}, expected {expected}, real {real}, result {expected == real}')
