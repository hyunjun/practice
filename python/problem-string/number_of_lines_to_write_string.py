#   https://leetcode.com/problems/number-of-lines-to-write-string

#   https://leetcode.com/problems/number-of-lines-to-write-string/solution


class Solution:
    #   35.83%
    def numberOfLines(self, widths, S):
        lines, curWidth = 0, 0
        for c in S:
            cur = widths[ord(c) - ord('a')]
            if curWidth + cur < 100:
                curWidth += cur
            elif curWidth + cur == 100:
                lines += 1
                curWidth = 0
            else:
                lines += 1
                curWidth = cur
        return [lines + 1, curWidth]


s = Solution()
data = [([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], 'abcdefghijklmnopqrstuvwxyz', [3, 60]),
        ([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], 'bbbcccdddaaa', [2, 4]),
        ]
for widths, S, expected in data:
    real = s.numberOfLines(widths, S)
    print('{}, {}, expected {}, real {}, result {}'.format(widths, S, expected, real, expected == real))
