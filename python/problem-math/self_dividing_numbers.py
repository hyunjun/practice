#   https://leetcode.com/problems/self-dividing-numbers

#   https://leetcode.com/problems/self-dividing-numbers/solution


class Solution:
    #   34.70%
    def selfDividingNumbers(self, left, right):
        def isSelfDivided(n):
            if 0 < n < 10:
                return True
            s = str(n)
            if '0' in s:
                return False
            numSet = set(s)
            if 1 == len(numSet):
                return True
            #numSet.remove('1')
            for num in numSet:
                if '1' == num:
                    continue
                if 0 != n % int(num):
                    return False
            return True
        return [i for i in range(left, right + 1) if isSelfDivided(i)]


s = Solution()
data = [(1, 22, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]),
        (1, 10000, []),
        ]
for left, right, expected in data:
    real = s.selfDividingNumbers(left, right)
    print('{}, {}, expected {}, real {}, result {}'.format(left, right, expected, real, expected == real))
