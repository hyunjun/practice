#   https://leetcode.com/problems/longest-chunked-palindrome-decomposition


class Solution:
    #   runtime; 40ms, 59.31%
    #   memory; 14MB, 100.00%
    def longestDecomposition0(self, text: str) -> int:
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

    #   runtime; 83.64%
    #   memory; 13.8MB, 100.00%
    def longestDecomposition(self, text: str) -> int:
        if text is None or 0 == len(text):
            return 0
        revText, i, j, splitNum = text[::-1], 0, 0, 0
        while i < len(text):
            j = i
            for k in range(i, len(text)):
                if text[k] != revText[j]:
                    continue
                if text[i:k + 1] == revText[j:j + k + 1 - i][::-1]:
                    i = k + 1
                    splitNum += 1
                    break
        return splitNum


s = Solution()
data = [('merchant', 1),
        ('aaa', 3),
        ('abba', 4),
        ('abcba', 5),
        ('antaprezatepzapreanta', 11),
        ('ghiabcdefhelloadamhelloabcdefghi', 7),
        ('vwsuvmbwknmnvwsuvmbwk', 5),
        ]
for text, expected in data:
    real = s.longestDecomposition(text)
    print(f'{text}, expected {expected}, real {real}, result {expected == real}')
