#   https://leetcode.com/problems/palindrome-number
#   89.85%


class Solution:
    def isPalindrome(self, x):
        s = str(x)
        return s == s[::-1]


s = Solution()
data = [(121, True), (-121, False)]
for num, expected in data:
    real = s.isPalindrome(num)
    print('{} expected {} real {} result {}'.format(num, expected, real, expected == real))
