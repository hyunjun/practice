#   https://leetcode.com/problems/letter-case-permutation

#   https://leetcode.com/problems/letter-case-permutation/discuss/115509/Python-simple-solution-(7-lines)


class Solution:
    #   15.88%
    def letterCasePermutation(self, S):
        if S is None or 0 == len(S):
            return S
        res = [S]
        for i in range(len(S)):
            if '0' <= S[i] <= '9':
                continue
            j = len(res)
            while j:
                s = res[j - 1]
                if 'a' <= s[i] <= 'z':
                    print(s[:i] + chr(ord(s[i]) - (ord('a') - ord('A'))) + s[i + 1:])
                    res.append(s[:i] + chr(ord(s[i]) - (ord('a') - ord('A'))) + s[i + 1:])
                elif 'A' <= s[i] <= 'Z':
                    print(s[:i] + chr(ord(s[i]) + (ord('a') - ord('A'))) + s[i + 1:])
                    res.append(s[:i] + chr(ord(s[i]) + (ord('a') - ord('A'))) + s[i + 1:])
                j -= 1
            print(res)
        return res


s = Solution()
data = [('a1b2', ['a1b2', 'a1B2', 'A1b2', 'A1B2']),
        ('3z4', ['3z4', '3Z4']),
        ('12345', ['12345']),
        ]
for S, expected in data:
    real = s.letterCasePermutation(S)
    print('{}, expected {}, real {}, result {}'.format(S, expected, real, sorted(expected) == sorted(real)))
