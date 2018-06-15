#   https://leetcode.com/problems/longest-palindrome
#   92.94%

#   https://leetcode.com/problems/longest-palindrome/solution


class Solution:
    def longestPalindrome(self, s):
        if s is None or 0 == len(s):
            return 0
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        res, isOddUsed = 0, False
        for k, v in d.items():
            if 0 == v % 2:
                res += v
            else:
                if isOddUsed:
                    res += v - 1
                else:
                    isOddUsed = True
                    res += v
        if not isOddUsed and 1 in d.values():
            res += 1
        return res


solution = Solution()
data = [('a', 1), ('abccccdd', 7), ('ccc', 3), ('cccddddd', 7)]
for s, expected in data:
    real = solution.longestPalindrome(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
