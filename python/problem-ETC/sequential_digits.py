#   https://leetcode.com/problems/sequential-digits


from typing import List


class Solution:
    #   https://leetcode.com/explore/featured/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3465
    #   runtime; 32ms, 53.33%
    #   memory; 13.8MB, 45.38%
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        the1stNum, numLen, numStrs, res = str(low)[0], len(str(low)), [], []
        while numLen <= len(str(high)):
            for i in range(numLen):
                digit = int(the1stNum) + i
                if digit <= 9:
                    numStrs.append(str(digit))
            curNum = int(''.join(numStrs))
            if curNum > high:
                break
            if low <= curNum and (0 == len(res) or (0 < len(res) and res[-1] < curNum)):
                res.append(curNum)
            if numStrs[-1] == '9':
                the1stNum = '1'
                numLen += 1
            else:
                the1stNum = str(int(the1stNum) + 1)
            numStrs.clear()
        return res


s = Solution()
data = [(100, 300, [123, 234]),
        (1000, 13000, [1234, 2345, 3456, 4567, 5678, 6789, 12345]),
        (3942, 8912, [4567, 5678, 6789]),
        (234, 2314, [234,345,456,567,678,789,1234]),
        (10, 1000000000, [12,23,34,45,56,67,78,89,123,234,345,456,567,678,789,1234,2345,3456,4567,5678,6789,12345,23456,34567,45678,56789,123456,234567,345678,456789,1234567,2345678,3456789,12345678,23456789,123456789]),
        ]
for low, high, expect in data:
    real = s.sequentialDigits(low, high)
    print(f'{low} {high} expect {expect} real {real} result {expect == real}')
'''
1st     '1'
numLen  3
for i in range(3):
i   digit   curNum
0   1 + 0   '1'
1   1 + 1   '2'
2   1 + 2   '3'
'''
