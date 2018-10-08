#   https://leetcode.com/problems/reverse-only-letters

#   https://leetcode.com/problems/reverse-only-letters/solution


class Solution:
    #   40ms
    def reverseOnlyLetters(self, S):
        if S is None or len(S) <= 1:
            return S

        def isAlpha(s):
            for c in s:
                if c < 'A' or 'Z' < c < 'a' or 'z' < c:
                    return False
            return True

        s = list(S)
        l, r = 0, len(s) - 1
        while l < r:
            while l < len(s) and False == isAlpha(s[l]):
                l += 1
            while -1 < r and False == isAlpha(s[r]):
                r -= 1
            if 0 <= l < r <= len(s) and isAlpha(s[l]) and isAlpha(s[r]):
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)


s = Solution()
data = [("ab-cd", "dc-ba"),
        ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
        ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!"),
        ]
for S, expected in data:
    real = s.reverseOnlyLetters(S)
    print('{}, expected {}, real {}, result {}'.format(S, expected, real, expected == real))
