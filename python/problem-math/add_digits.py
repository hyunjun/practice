#   https://leetcode.com/problems/add-digits


class Solution:
    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3402
    #   runtime; 36ms, 50.83%
    #   memory; 14MB, 19.65%
    def addDigitsRecur(self, num):
        strNum = str(num)
        if 1 == len(strNum):
            return num
        return self.addDigits(sum([int(n) for n in strNum]))

    #   40.26%
    def addDigitsIter(self, num):
        while True:
            strNum = str(num)
            if 1 == len(strNum):
                break
            num = sum([int(n) for n in strNum])
        return num

    #   https://leetcode.com/problems/add-digits/discuss/68667/Simple-Java-Solution-No-recursion-loop
    #   92.08%
    #   10^k % 9 = 1
    #   a*10^k % 9 = a % 9
    def addDigits(self, num):
        if 0 == num:
            return 0
        if 0 == num % 9:
            return 9;
        return num % 9


s = Solution()
data = [(38, 2),
        (23456, 2),
        ]
for num, expect in data:
    real = s.addDigits(num)
    print('{}, expect {}, real {}, result {}'.format(num, expect, real, expect == real))
