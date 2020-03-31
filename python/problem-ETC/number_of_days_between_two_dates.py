#   https://leetcode.com/problems/number-of-days-between-two-dates


class Solution:
    #   runtime; 32ms, 25.32%
    #   memory; 13.8MB, 100.00%
    def daysBetweenDates(self, date1: str, date2: str) -> int:

        shorter, bigger = date1, date2
        if date1 > date2:
            shorter, bigger = date2, date1

        def getYMD(dateStr):
            y, m, d = dateStr.split('-')
            return int(y), int(m), int(d)

        sy, sm, sd = getYMD(shorter)
        ey, em, ed = getYMD(bigger)

        def isLunarYear(y):
            return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

        def isLunarYearFeb(m, y):
            return m == 2 and isLunarYear(y)

        days, days_dict = 0, {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        if sy != ey:
            days += days_dict[sm] - sd
            if isLunarYearFeb(sm, sy):
                days += 1
            for m in range(sm + 1, 13):
                days += days_dict[m]
                if isLunarYearFeb(m, sy):
                    days += 1
            for y in range(sy + 1, ey):
                days += 365
                if isLunarYear(y):
                    days += 1
            for m in range(1, em):
                days += days_dict[m]
                if isLunarYearFeb(m, ey):
                    days += 1
            days += ed
        else:
            if sm != em:
                days += days_dict[sm] - sd
                if isLunarYearFeb(sm, sy):
                    days += 1
                for m in range(sm + 1, em):
                    days += days_dict[m]
                    if isLunarYearFeb(m, sy):
                        days += 1
                days += ed
            else:
                days += ed - sd
        return days


s = Solution()
data = [('2019-06-29', '2019-06-30', 1),
        ('2020-01-15', '2019-12-31', 15),
        ('1996-01-15', '1996-12-31', 351),
        ('1997-01-15', '1997-12-31', 350),
        ('1996-01-15', '2001-12-30', 2176),
        ('1971-01-05', '2100-12-30', 47476),
        ]
for date1, date2, expected in data:
    real = s.daysBetweenDates(date1, date2)
    print(f'{date1} {date2} expected {expected} real {real} result {expected == real}')
