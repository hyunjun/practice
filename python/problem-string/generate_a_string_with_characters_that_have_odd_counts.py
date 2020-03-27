# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts


class Solution:
    #   runtime; 20ms, 96.58%
    #   memory; 13.8MB, 100.00%
    def generateTheString(self, n: int) -> str:
        if not (1 <= n <= 500):
            return ''
        if n == 1:
            return 'a'
        if n % 2 == 0:
            return 'a' * (n - 1) + 'b'
        return 'a' * (n - 2) + 'b' + 'c'


s = Solution()
for i in [2, 4, 7]:
    print(s.generateTheString(i))
