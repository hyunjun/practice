#   https://leetcode.com/problems/longest-chunked-palindrome-decomposition


class Solution:
    #   runtime; 40ms, 59.31%
    #   memory; 14MB, 100.00%
    def longestDecomposition(self, text: str) -> int:
        if text is None or 0 == len(text):
            return 0
        l, r, splitNum = 0, len(text) - 1, 0
        while l <= r:
            for i in range(r - l + 1):
                if text[l:l + i + 1] == text[r - i:r + 1]:
                    if l == r - i:
                        splitNum += 1
                    else:
                        splitNum += 2
                    l = l + i + 1
                    r = r - i - 1
                    break
        return splitNum


s = Solution()
data = [('ghiabcdefhelloadamhelloabcdefghi', 7),
        ('merchant', 1),
        ('antaprezatepzapreanta', 11),
        ('aaa', 3),
        ('abcba', 5),
        ('abba', 4),
        ]
for text, expected in data:
    real = s.longestDecomposition(text)
    print(f'{text}, expected {expected}, real {real}, result {expected == real}')
