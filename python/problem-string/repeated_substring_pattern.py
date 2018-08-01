#   https://leetcode.com/problems/repeated-substring-pattern

#   https://leetcode.com/problems/repeated-substring-pattern/discuss/94455/1-line-in-Python


class Solution:
    #   63.25%
    def repeatedSubstringPattern(self, s):
        if s is None or len(s) <= 1:
            return False
        if 1 == len(set(s)):
            return True
        def numbers(n):
            res = set()
            if 0 == n % 2:
                s = n // 2
                e = 0
                while s >= e:
                    if 0 == n % s:
                        res.add(s)
                        e = n // s
                        if e < n:
                            res.add(e)
                    else:
                        e += 1
                    s -= 2
            else:
                s = 3
                e = n // 2
                while s < n and s < e:
                    if 0 == n % s:
                        res.add(s)
                        e = n // s
                        res.add(e)
                    else:
                        e -= 1
                    s += 2
            return list(res)
        nums = numbers(len(s))
        for num in nums:
            #print(num, s[:num] * (len(s) // num))
            if s[:num] * (len(s) // num) == s:
                return True
        return False


solution = Solution()
data = [('abab', True),
        ('aba', False),
        ('abcabcabcabc', True),
        ('abcabcabc', True),
        ('bb', True),
        ('ab', False),
        ('zzz', True),
        ('a', False),
        ]
for s, expected in data:
    real = solution.repeatedSubstringPattern(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
