#   https://leetcode.com/problems/fizz-buzz

#   https://leetcode.com/problems/fizz-buzz/discuss/136170/Interesting-Python-1-line-solution-Explained


from typing import List


class Solution:
    #   27.04%
    def fizzBuzz0(self, n):
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

    #   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3437
    #   runtime; 52ms, 43.41%
    #   memory; 14.8MB, 70.24%
    def fizzBuzz(self, n: int) -> List[str]:
        def getValue(num):
            ret = []
            if num % 3 == 0:
                ret.append('Fizz')
            if num % 5 == 0:
                ret.append('Buzz')
            return str(num) if 0 == len(ret) else ''.join(ret)
        return [getValue(i) for i in range(1, n + 1)]


s = Solution()
print(s.fizzBuzz(15))
