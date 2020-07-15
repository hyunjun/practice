#   https://leetcode.com/problems/reformat-date


class Solution:
    #   runtime; 52ms, 100.00%
    #   memory; 13.8MB, 100.00%
    def reformatDate(self, date: str) -> str:
        dayDict = {f'{n}th': str(n) if n > 9 else '0' + str(n) for n in range(4, 31)}
        dayDict['1st'] = '01'
        dayDict['2nd'] = '02'
        dayDict['3rd'] = '03'
        dayDict['21st'] = '21'
        dayDict['22nd'] = '22'
        dayDict['23rd'] = '23'
        dayDict['31st'] = '31'
        monthDict = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "May": '05', "Jun": '06', "Jul": '07', "Aug": '08', "Sep": '09', "Oct": '10', "Nov": '11', "Dec": '12'}
        day, month, year = date.split(' ')
        return f'{year}-{monthDict[month]}-{dayDict[day]}'


s = Solution()
data = [("20th Oct 2052", "2052-10-20"),
        ("6th Jun 1933", "1933-06-06"),
        ("26th May 1960", "1960-05-26"),
        ("12th Apr 2023", "2023-04-12"),
        ]
for date, expect in data:
    real = s.reformatDate(date)
    print(f'{date} expect {expect} real {real} result {expect == real}')
