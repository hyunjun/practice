#   https://leetcode.com/problems/basic-calculator-ii


class Solution:
    #   https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/567/week-4-november-22nd-november-28th/3542
    #   runtime; 136ms, 18.49%
    #   memory; 18.8MB, 6.92%
    def calculate(self, s: str) -> int:
        p, exp = 0, []
        for i, c in enumerate(s):
            if c in ['+', '-', '*', '/']:
                exp.append(int(s[p:i]))
                exp.append(c)
                p = i + 1
        exp.append(int(s[p:]))
        for i, op in enumerate(exp):
            if op  == '*':
                exp[i + 1] *= exp[i - 1]
                exp[i - 1] = exp[i] = None
            elif op == '/':
                exp[i + 1] = exp[i - 1] // exp[i + 1]
                exp[i - 1] = exp[i] = None
        exp = [op for op in exp if op is not None]
        for i, op in enumerate(exp):
            if op  == '+':
                exp[i + 1] += exp[i - 1]
                exp[i - 1] = exp[i] = None
            elif op == '-':
                exp[i + 1] = exp[i - 1] - exp[i + 1]
                exp[i - 1] = exp[i] = None
        return [op for op in exp if op is not None][0]


solution = Solution()
data = [("3+2*2", 7),
        (" 3/2 ", 1),
        (" 3+5 / 2 ", 5),
        ]
for s, expect in data:
    real = solution.calculate(s)
    print(f'{s} expect {expect} real {real} result {expect == real}')
