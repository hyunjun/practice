#   https://leetcode.com/problems/length-of-last-word
#   96.86%


class Solution:
    def lengthOfLastWord(self, s):
        if s is None or 0 == len(s):
            return 0
        s = s.strip()
        idx = len(s) - 1
        while 0 < idx and ' ' != s[idx]:
            idx -= 1
        if 0 == idx:
            return len(s)
        return len(s) - idx - 1


s = Solution()
data = [("Hello World", 5), ("Hello World ", 5), ("a", 1), (" ", 0)]
for inp, expected in data:
    real = s.lengthOfLastWord(inp)
    print('{}, expected {}, real {}, result {}'.format(inp, expected, real, expected == real))
