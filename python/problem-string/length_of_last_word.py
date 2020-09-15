#   https://leetcode.com/problems/length-of-last-word


class Solution:
    #   runtime; 36ms, 96.86%
    def lengthOfLastWord0(self, s):
        if s is None or 0 == len(s):
            return 0
        s = s.strip()
        idx = len(s) - 1
        while 0 < idx and ' ' != s[idx]:
            idx -= 1
        if 0 == idx:
            return len(s)
        return len(s) - idx - 1

    #   https://leetcode.com/explore/featured/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3461
    #   runtime; 32ms, 53.45%
    #   memory; 13.7MB, 94.00%
    def lengthOfLastWord1(self, s: str) -> int:
        return 0 if s is None or len(s) == 0 or len(s.split()) == 0 else len(s.split()[-1])

    #   runtime; 32ms, 53.45%
    #   memory; 13.8MB, 90.79%
    def lengthOfLastWord(self, s: str) -> int:
        if s is None:
            return 0
        end = len(s) - 1
        while 0 <= end and s[end] == ' ':
            end -= 1
        start = end
        while 0 <= start and s[start] != ' ':
            start -= 1
        return end - start if start <= end else 0


solution = Solution()
data = [("Hello World", 5),
        ("Hello World ", 5),
        ("a", 1),
        (" ", 0),
        ]
for s, expect in data:
    real = solution.lengthOfLastWord(s)
    print(f'{s}, expect {expect}, real {real}, result {expect == real}')
