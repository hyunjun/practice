#   https://leetcode.com/problems/maximum-repeating-substring


class Solution:
    #   runtime; 32ms, 66.71%
    #   memory; 14.3MB, 14.74%
    def maxRepeating(self, sequence: str, word: str) -> int:
        check, n, ret = word, 1, 0
        while len(check) <= len(sequence):
            if check in sequence:
                ret = max(ret, n)
            n += 1
            check += word
        return ret


s = Solution()
data = [("a", "a", 1),
        ("ababc", "ab", 2),
        ("ababc", "ba", 1),
        ("ababc", "ac", 0),
        ("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba", 5),
        ]
for sequence, word, expect in data:
    real = s.maxRepeating(sequence, word)
    print(f'{sequence} {word} expect {expect} real {real} result {expect == real}')
