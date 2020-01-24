#   https://leetcode.com/problems/maximum-69-number


class Solution:
    #   runtime; 44ms, 8.28%
    #   memory; 12.4MB, 100.00%
    def maximum69Number (self, num: int) -> int:
        if not (1 <= num <= 10 ** 4):
            return 0
        maxNum, l = num, list(str(num))
        for i in range(len(l)):
            cand = int(''.join(l[:i] + ['9'] + l[i + 1:] if l[i] == '6' else l[:i] + ['6'] + l[i + 1:]))
            if maxNum < cand:
                maxNum = cand
        return maxNum


s = Solution()
data = [(9669, 9969),
        (9996, 9999),
        (9999, 9999),
        ]
for num, expected in data:
    real = s.maximum69Number(num)
    print(f'{num} expected {expected} real {real} result {expected == real}')
