#   https://leetcode.com/problems/mirror-reflection


class Solution:
    #   https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3534
    #   runtime; 24ms, 91.58%
    #   memory; 14.1MB, 72.98%
    def mirrorReflection(self, p: int, q: int) -> int:

        def gcd(a, b):
            while a != b:
                if a > b:
                    a -= b
                else:
                    b -= a
            return a

        if p == q:
            return 1
        g = gcd(p, q)
        p, q = p // g, q // g
        if p % q == 0:
            p, q = p // q, 1
        if p % 2 == 0:
            return 2
        if q % 2 == 0:
            return 0
        return 1


s = Solution()
data = [(2, 1, 2),
        (9, 7, 1),
        (6, 2, 1),
        (7, 4, 0),
        (6, 4, 0),
        ]
for p, q, expect in data:
    real = s.mirrorReflection(p, q)
    print(f'{p} {q} expect {expect} real {real} result {expect == real}')

'''
처음엔 반사각에 따라 왔다갔다 하는 좌표를 구하려고 했으나 복잡해져서 포기

2차원 좌표계에서 그냥 y = (q / p) * x의 방정식에 따라 좌표가 np, mp로 p의 배수가 되는 경우를 생각해봄
그렇게 하면, x, y가 (np, mp)가 되는 경우 mirror에 만나는 거고, 짝수냐 홀수냐에 따라 mirror의 번호를 결정할 수 있음
'''
