#   https://leetcode.com/problems/determine-if-string-halves-are-alike


class Solution:
    #   runtime: 36 ms, 65.55%
    #   memory: 14.3 MB, 68.01%
    def halvesAreAlike0(self, s: str) -> bool: 
        m, s, vowels, c = len(s) // 2, s.lower(), set(['a', 'e', 'i', 'o', 'u']), 0
        for i in range(m):
            if s[i] in vowels:
                c += 1
        for i in range(m, len(s)):
            if s[i] in vowels:
                c -= 1
        return c == 0

    #   lower()를 사용하지 않고 vowels에서 대소문자 모두 처리
    #   runtime: 32 ms, 85.83%
    #   memory Usage: 14.5 MB, 9.61%
    def halvesAreAlike(self, s: str) -> bool: 
        m, vowels, c = len(s) // 2, set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']), 0
        for i in range(m):
            if s[i] in vowels:
                c += 1
        for i in range(m, len(s)):
            if s[i] in vowels:
                c -= 1
        return c == 0


solution = Solution()
data = [("book", True),
        ("textbook", False),
        ("MerryChristmas", False),
        ("AbCdEfGh", True),
        ]
for s, expect in data:
    real = solution.halvesAreAlike(s)
    print(f'{s} expect {expect} real {real} result {expect == real}')
