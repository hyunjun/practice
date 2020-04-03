#   https://leetcode.com/problems/remove-palindromic-subsequences

#   https://leetcode.com/problems/remove-palindromic-subsequences/discuss/529885/Java-0ms-Video-Explanation


class Solution:
    #   Wrong Answer
    def removePalindromeSub0(self, s: str) -> int:
        if s is None or not (0 <= len(s) <= 1000):
            return 0

        def isPalindrome(l):
            return l == l[::-1]

        d = {}
        def removePalindrome(sub):
            print(sub)
            if sub in d:
                return d[sub]
            if len(sub) == 0:
                return 0
            if len(sub) == 1 and isPalindrome(sub):
                return 1
            ret = min(removePalindrome(sub[1:]), removePalindrome(sub[:-1])) + 1
            d[sub] = ret
            return ret

        return removePalindrome(s)

    #   Wrong Answer
    def removePalindromeSub1(self, s: str) -> int:
        if s is None or not (0 <= len(s) <= 1000):
            return 0

        d = {'a': 0, 'b': 0}
        for c in s:
            d[c] += 1
        print(d)

        cnt, lStr = 0, list(s)
        while 0 < len(lStr):
            l, r = 0, len(lStr) - 1
            while l <= r:
                print(lStr, l, r, d)
                if l == r:
                    d[lStr[l]] -= 1
                    lStr[l] = None
                    break
                if lStr[l] == lStr[r]:
                    d[lStr[l]] -= 2
                    lStr[l] = lStr[r] = None
                    l += 1
                    r -= 1
                else:
                    if d['a'] > d['b']:
                        if lStr[r] == 'b':
                            r -= 1
                        else:
                            l += 1
                    else:   #   if len(d['a']) < len(d['b'])
                        if lStr[l] == 'a':
                            l += 1
                        else:
                            r -= 1
            lStr = [c for c in lStr if c]
            cnt += 1

        return cnt

    #   runtime; 32ms, 12.18%
    #   memory; 13.9MB, 100.00%
    def removePalindromeSub(self, s: str) -> int:
        if s is None or 0 == len(s) or not (0 < len(s) <= 1000):
            return 0

        if s == s[::-1]:
            return 1
        return 2


solution = Solution()
data = [('ababa', 1),
        ('abb', 2),
        ('baabb', 2),
        ('', 0),
        ('aaaaabbbabbbaaaaaabbbaaaaaaaabbbaaaaa', 2),
        ]
for s, expected in data:
    real = solution.removePalindromeSub(s)
    print(f'{s} expected {expected} real {real} result {expected == real}')
