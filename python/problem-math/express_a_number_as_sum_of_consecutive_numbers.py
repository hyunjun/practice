#   https://www.youtube.com/watch?v=5Kl8q9kqlNg


class Solution:
    def sumOfConsecutiveNumbers(self, n):
        if n % 2 == 1:
            return [n // 2, n // 2 + 1]
        d = (n - 2) // 4
        if d * 4 + 2 == n:
            return [d - 1, d, d + 1, d + 2]
        return []


s = Solution()
data = [(10, [[1, 2, 3, 4]]),
        (15, [[7, 8], [4, 5, 6], [1, 2, 3, 4, 5]]),
       ]
for n, expecteds in data:
    result, real = False, s.sumOfConsecutiveNumbers(n)
    for e in expecteds:
        if e == real:
            result = True
            break
    print(f'{n} expected {expecteds} real {real} result {result}')
