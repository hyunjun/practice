#   https://leetcode.com/problems/nth-digit
#   47.33%


class Solution:
    def findNthDigit(self, n):
        digitNum, startRange = 1, 1
        while True:
            start = 10 ** (digitNum - 1)
            end = 10 ** digitNum - 1
            digitCnt = (end - start + 1) * digitNum
            endRange = startRange + digitCnt

            if startRange <= n < endRange:
                print('start {}, n {}, cur end {}'.format(startRange, n, endRange))
                number = start + (n - startRange) // digitNum
                idx = (n - startRange) % digitNum
                return int(str(number)[idx])

            digitNum += 1
            startRange = endRange

        return None


s = Solution()
data = [(3, 3), (11, 0), (30, 2), (31, 0), (190, 1), (191, 0), (192, 0)]
for n, expected in data:
    real = s.findNthDigit(n)
    print('{}, expected {}, real {}, result {}'.format(n, expected, real, expected == real))
'''
digitNum    start   end     digitCnt                    range
1           1       9       (9 - 1 + 1) * 1 = 9         1~10
2           10      99      (99 - 10 + 1) * 2 = 180     10~190
3           100     999     (999 - 100 + 1) * 3 = 2700  190~2890
'''
