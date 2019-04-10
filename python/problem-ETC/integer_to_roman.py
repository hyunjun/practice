#   https://leetcode.com/problems/integer-to-roman


class Solution:
    #   runtime; 56ms, 99.87%
    #   memory; 13.3MB, 5.14%
    def intToRoman0(self, num):
        ret = []
        if 1000 <= num:
            ret.append('M' * (num // 1000))
            num %= 1000
        if 100 <= num:
            d = num // 100
            if 9 == d:
                ret.append('CM')
            elif 5 <= d <= 8:
                ret.append('D')
                ret.append('C' * (d - 5))
            elif 4 == d:
                ret.append('CD')
            else:
                ret.append('C' * d)
            num %= 100
        if 10 <= num:
            d = num // 10
            if 9 == d:
                ret.append('XC')
            elif 5 <= d <= 8:
                ret.append('L')
                ret.append('X' * (d - 5))
            elif 4 == d:
                ret.append('XL')
            else:
                ret.append('X' * d)
            num %= 10
        if 9 == num:
            ret.append('IX')
        elif 5 <= num <= 8:
            ret.append('V')
            ret.append('I' * (num - 5))
        elif 4 == num:
            ret.append('IV')
        else:
            ret.append('I' * num)
        return ''.join(ret)

    #   runtime; 64ms, 93.33%
    #   memory; 13.4MB, 5.14%
    def intToRoman(self, num):
        ret = []
        if 1000 <= num:
            ret.append('M' * (num // 1000))
            num %= 1000
        numDicts = {100: {9: 'CM', 5: 'D', 4: 'CD', 1: 'C'}, 10: {9: 'XC', 5: 'L', 4: 'XL', 1: 'X'}, 1: {9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}}
        for n, nDict in sorted(numDicts.items(), key=lambda t: -t[0]):
            if n <= num:
                d = num // n
                if 9 == d or 4 == d:
                    ret.append(nDict[d])
                elif 5 <= d:
                    ret.append(nDict[5])
                    ret.append(nDict[1] * (d - 5))
                else:
                    ret.append(nDict[1] * d)
                num %= n
        return ''.join(ret)


s = Solution()
data = [(3, 'III'),
        (4, 'IV'),
        (9, 'IX'),
        (58, 'LVIII'),
        (1994, 'MCMXCIV'),
        ]
for num, expected in data:
    real = s.intToRoman(num)
    print('{}, expected {}, real {}, result {}'.format(num, expected, real, expected == real))
