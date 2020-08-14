#   https://leetcode.com/problems/longest-palindrome

#   https://leetcode.com/problems/longest-palindrome/solution


from collections import Counter


class Solution:
    #   92.94%
    def longestPalindrome0(self, s):
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

    #   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3423
    #   runtime; 32ms, 76.65%
    #   memory; 14.1MB
    def longestPalindrome(self, s: str) -> int:
        cnt, hasOdd = 0, False
        for val in Counter(s).values():
            if val % 2 == 0:
                cnt += val
            else:
                hasOdd = True
                cnt += val - 1
        if hasOdd:
            return cnt + 1
        return cnt
        


solution = Solution()
data = [('a', 1),
        ('abccccdd', 7),
        ('ccc', 3),
        ('cccddddd', 7),
        ]
for s, expect in data:
    real = solution.longestPalindrome(s)
    print(f'{s}, expect {expect}, real {real}, result {expect == real}')
