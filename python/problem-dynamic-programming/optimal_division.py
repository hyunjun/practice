#   https://leetcode.com/problems/optimal-division

#   https://leetcode.com/problems/optimal-division/solution


class Solution:
    #   Wrong Answer
    def optimalDivision0(self, nums):
        if nums is None or 0 == len(nums):
            return None
        pre = [0] * len(nums)
        pre[-1] = nums[-1]
        paren = [False] * len(nums)
        for i in range(len(nums) - 2, 0, -1):
            print(pre)
            print(i, nums[i], pre[i + 1])
            a = float(nums[i]) / pre[i + 1]
            b = float(nums[i])
            for j in range(i + 1, len(nums)):
                b /= nums[j]
            print(a, b)
            if b < a:
                pre[i] = b
                paren[i] = True
            else:
                pre[i] = a
                if i != len(nums) - 2:
                    paren[i + 1] = True
        res, parenCnt = [], 0
        for i, n in enumerate(nums):
            if paren[i]:
                res.append('(')
                parenCnt += 1
            if i == len(nums) - 1:
                res.append(str(n))
            else:
                res.append('{}/'.format(n))
        while parenCnt:
            res.append(')')
            parenCnt -= 1
        return ''.join(res)

    #   1.61%
    def optimalDivision(self, nums):
        if nums is None or 0 == len(nums):
            return None
        if 1 == len(nums):
            return str(nums[0])
        if 2 == len(nums):
            return '{}/{}'.format(nums[0], nums[1])
        self.mul, self.res = 0, None
        def addParen(parens, idx):
            if idx == len(nums) - 2:
                #print(nums)
                #print(parens)
                exp, calcExp, openCnt = [], [], 0
                for i, n in enumerate(nums):
                    exp.append(str(n))
                    calcExp.append('float({})'.format(n))
                    if i < len(nums) - 1:
                        exp.append(parens[i])
                        calcExp.append(parens[i])
                        if 2 == len(parens[i]):
                            openCnt += 1
                exp.append(')' * openCnt)
                calcExp.append(')' * openCnt)
                mul = eval(''.join(calcExp))
                #print(mul, ''.join(exp))
                if self.mul <= mul:
                    self.mul, self.res = mul, ''.join(exp)
            else:
                addParen(parens[:], idx + 1)
                parens[idx] = '/('
                addParen(parens[:], idx + 1)
        addParen(['/'] * (len(nums) - 1), 0)
        return self.res


s = Solution()
data = [([1000, 100, 10, 2], '1000/(100/10/2)'),
        ([1000, 100, 10, 2, 1, 5], '1000/(100/10/(2/(1/5)))'),
        ]
for nums, expected in data:
    real = s.optimalDivision(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
'''
1000
100
10      10/2/1/5    10/(2/1/5)  10/2/(1/5)  10/(2/(1/5))
2       2/1/5                   2/(1/5)
1       1/5
5
'''
