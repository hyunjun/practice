#   https://leetcode.com/problems/angle-between-hands-of-a-clock


class Solution:
    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3390
    #   runtime; 56ms, 7.28%
    #   memory; 13.9MB, 43.72%
    def angleClock0(self, hour: int, minutes: int) -> float:
        if not (1 <= hour <= 12) or not (0 <= minutes <= 59):
            return float('-inf')
        ret = abs(30 * ((0 if hour == 12 else hour) + minutes / 60) - 6 * minutes)
        return ret if ret < 180 else 360 - ret

    #   runtime; 32ms, 52.48%
    #   memory; 13.8MB, 53.49%
    def angleClock(self, hour: int, minutes: int) -> float:
        if not (1 <= hour <= 12) or not (0 <= minutes <= 59):
            return float('-inf')
        ret = abs(30 * (hour % 12 + minutes / 60) - 6 * minutes)
        return min(ret, 360 - ret)


s = Solution()
data = [(12, 30, 165),
        (3, 30, 75),
        (3, 15, 7.5),
        (4, 50, 155),
        (12, 0, 0),
        (1, 57, 76.5),
        ]
for hour, minutes, expect in data:
    real = s.angleClock(hour, minutes)
    print(f'{hour} {minutes} expect {expect} real {real} result {expect == real}')
