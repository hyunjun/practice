#   https://leetcode.com/problems/day-of-the-week

#   https://leetcode.com/problems/day-of-the-week/discuss/432040/Python-simply-calculate-different-days-with-given-known-date


import datetime


class Solution(object):
    WEEKDAY = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
               4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    
    #   runtime; 16ms, 67.68%
    #   memory; 11.8MB, 100.00%
    def dayOfTheWeek(self, day, month, year):
        return Solution.WEEKDAY[datetime.date(year, month, day).weekday()]


s = Solution()
data = [(31, 8, 2019, 'Saturday'),
        (18, 7, 1999, 'Sunday'),
        (15, 8, 1993, 'Sunday'),
        ]
for day, month, year, expected in data:
    real = s.dayOfTheWeek(day, month, year)
    print(f'{day}, {month}, {year}, expected {expected}, real {real}, result {expected == real}')
