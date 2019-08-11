#   https://leetcode.com/problems/day-of-the-year


class Solution:
    #   runtime; 32ms, 100.00%
    #   memory; 13.7MB, 100.00%
    def dayOfYear(self, date: str) -> int:
        if str is None or 10 != len(date):
            return 0
        total, year, month, day = 0, int(date[:4]), int(date[5:7]), int(date[8:])
        for m in range(1, month):
            if m == 2:
                if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                    total += 29
                else:
                    total += 28
            elif m in [1, 3, 5, 7, 8, 10, 12]:
                total += 31
            else:
                total += 30
        return total + day


s = Solution()
data = [('2019-01-09', 9),
        ('2019-02-10', 41),
        ('2003-03-01', 60),
        ('2004-03-01', 61),
        ]
for date, expected in data:
    real = s.dayOfYear(date)
    print(f'{date}, expected {expected}, real {real}, result {expected == real}')
