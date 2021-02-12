#   https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero


class Solution:
    #   runtime; 20ms, 96.86%
    #   memory; 13.9MB, 100.00%
    def numberOfSteps0(self, num: int) -> int:
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

    #   https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3637
    #   runtime; 32ms, 63.53%
    #   memory; 14.2MB, 39.48%
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while 0 < num:
            if num & 1 == 1:
                num -= 1
            else:
                num //= 2
            cnt += 1
        return cnt


s = Solution()
data = [(14, 6),
        (8, 4),
        (123, 12),
        ]
for num, expect in data:
    real = s.numberOfSteps(num)
    print(f'{num} expect {expect} real {real} result {expect == real}')
