#   https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero


class Solution:
    #   runtime; 20ms, 96.86%
    #   memory; 13.9MB, 100.00%
    def numberOfSteps (self, num: int) -> int:
        if not (0 <= num <= 10 ** 6):
            return 0
        cnt = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            cnt += 1
        return cnt


s = Solution()
data = [(14, 6),
        (8, 4),
        (123, 12),
        ]
for num, expected in data:
    real = s.numberOfSteps(num)
    print(f'{num} expected {expected} real {real} result {expected == real}')
