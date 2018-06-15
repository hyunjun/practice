#   https://leetcode.com/problems/add-strings
#   69.20%


class Solution:
    def addStrings(self, num1, num2):
        if num1 is None or 0 == len(num1):
            return num2
        if num2 is None or 0 == len(num2):
            return num1
        lenShort = len(num1)
        if len(num2) < len(num1):
            num1, num2 = num2, num1
            lenShort = len(num1)
        n1, n2, res, carry = num1[::-1], num2[::-1], [], 0
        for i in range(lenShort):
            cur = int(n1[i]) + int(n2[i]) + carry
            if 9 < cur:
                carry = 1
                cur -= 10
            else:
                carry = 0
            res.append(str(cur))
        for i in range(lenShort, len(num2)):
            cur = int(n2[i]) + carry
            if 9 < cur:
                carry = 1
                cur -= 10
            else:
                carry = 0
            res.append(str(cur))
        if 1 == carry:
            res.append('1')
        return ''.join(res[::-1])


s = Solution()
data = [('189', '32', '221'), ('1', '9', '10')]
for num1, num2, expected in data:
    real = s.addStrings(num1, num2)
    print('{} + {} = expected {}, real {}, result {}'.format(num1, num2, expected, real, expected == real))
'''
num1    num2    lenShort
189     32
32      189     2
n1      n2      res     carry
23      981             0
i       cur
0       2 + 9 + 0 = 11
        1               1
                1
1       3 + 8 + 1 = 12
        2               1
                1 2
2       1 + 1 = 2       0
        2       1 2 2
221
'''
