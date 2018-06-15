#   https://leetcode.com/problems/fizz-buzz
#   27.04%

#   https://leetcode.com/problems/fizz-buzz/discuss/136170/Interesting-Python-1-line-solution-Explained


class Solution:
    def fizzBuzz(self, n):
        if n <= 0:
            return []
        res = []
        for i in range(1, n + 1):
            mod3, mod5 = i % 3, i % 5
            if 0 == mod3 and 0 == mod5:
                res.append('FizzBuzz')
            elif 0 == mod3:
                res.append('Fizz')
            elif 0 == mod5:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res


s = Solution()
print(s.fizzBuzz(15))
