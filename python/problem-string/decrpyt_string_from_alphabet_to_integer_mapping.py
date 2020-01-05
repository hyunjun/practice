#   https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping

#   https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/discuss/470867/Python-1-line-Regex


class Solution:
    #   runtime; 24ms, 50.00%
    #   memory; 12.7MB, 100.00%
    def freqAlphabets(self, s: str) -> str:
        if s is None or not (1 <= len(s) <= 1000):
            return ''

        res, i = [], len(s) - 1
        while 0 <= i:
            if s[i] == '#':
                n = int(s[i - 2:i])
                i -= 3
            else:
                n = int(s[i])
                i -= 1
            res.append(chr(n + 96))
        return ''.join(res[::-1])


solution = Solution()
data = [("10#11#12", "jkab"),
        ("1326#", "acz"),
        ("25#", "y"),
        ("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#", "abcdefghijklmnopqrstuvwxyz"),
        ]
for s, expected in data:
    real = solution.freqAlphabets(s)
    print(f'{s} expected {expected} real {real} result {expected == real}')
