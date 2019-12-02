#   https://leetcode.com/problems/hexspeak


class Solution:
    #   runtime; 40ms, 6.70%
    #   memory; 12.7MB, 100.00%
    def toHexspeak0(self, num: str) -> str:
        if num is None or 0 == len(num):
            return 'ERROR'

        validHexNums = {0: 'O', 1: 'I', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        def numToHexStr(n):
            n = int(n)
            maxSup = 0
            for i in range(1, 11):
                if n < 16 ** i:
                    maxSup = i - 1
                    break
            res, hexNum = [], 16 ** maxSup
            while 0 < maxSup:
                if hexNum <= n:
                    res.append(n // hexNum)
                    n %= hexNum
                else:
                    res.append(0)
                hexNum //= 16
                maxSup -= 1
            res.append(n)
            for i, r in enumerate(res):
                if r in validHexNums:
                    res[i] = validHexNums[r]
                else:
                    res[i] = str(r)
            return res
            
        hexStr = numToHexStr(num)
        for c in hexStr:
            if c not in validHexNums.values():
                return 'ERROR'
        return ''.join(hexStr)

    #   runtime; 32ms, 34.87%
    #   memory; 12.6MB, 100.00%
    def toHexspeak(self, num: str) -> str:
        if num is None or 0 == len(num):
            return 'ERROR'

        validHexNums = {'0': 'O', '1': 'I', 'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F'}
        hexStr = [validHexNums[i] if i in validHexNums else i for i in hex(int(num))[2:]]
        for c in hexStr:
            if c not in validHexNums.values():
                return 'ERROR'
        return ''.join(hexStr)


s = Solution()
data = [('257', 'IOI'),
        ('3', 'ERROR'),
        ("747823223228", "AEIDBCDIBC"),
        ("12431616", "BDBIOO"),
        ]
for num, expected in data:
    real = s.toHexspeak(num)
    print(f'{num}, expected {expected}, real {real}, result {expected == real}')
