#   https://leetcode.com/problems/palindromic-substrings

#   https://leetcode.com/problems/palindromic-substrings/solution


from collections import defaultdict

class Solution:
    #   runtime; 1004ms, 9.51%
    #   memory; 227.4MB, 100.00%
    def countSubstrings(self, s):
        if s is None or 0 == len(s):
            return 0

        d = defaultdict(bool)
        def isPalindrome(_s):
            if _s in d:
                return d[_s]
            if _s == _s[::-1]:
                d[_s] = True
            return d[_s]

        cnt = len(s)
        for l in range(2, len(s) + 1):
            for start in range(0, len(s)):
                if len(s) < start + l:
                    break
                if isPalindrome(s[start:start + l]):
                    cnt += 1
        return cnt


s = Solution()
data = [('abc', 3),
        ('aaa', 6),
        ]
for _s, expected in data:
    real = s.countSubstrings(_s)
    print('{}, expected {}, real {}, result {}'.format(_s, expected, real, expected == real))
