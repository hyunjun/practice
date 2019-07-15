#   https://stackoverflow.com/questions/51312279/python-floating-point-precision-sum


from decimal import Decimal
import math


A, B, C, D, E = [0.129967], [0.815911, 0.917844], [0.107228], [0.487474], [1.930395, 1.256333, 1.21594]
print(f'A {A}, B {B}, C {C}, D {D}, E {E}')
exprs = ['sum(A[0], B[0:2])',
         'sum(B[0:2], A[0])',
         'sum(C[0], D[0], E[0])',
         'sum(sum(C[0], D[0]), E[0])',
         'sum(C[0], D[0])',
         'math.fsum([C[0], D[0]])',
         'Decimal(C[0]) + Decimal(D[0])'
         ]
for expr in exprs:
    try:
        print('{}\t{}'.format(expr, eval(expr)))
    except TypeError as e:
        print('{}\t{}'.format(expr, e))
