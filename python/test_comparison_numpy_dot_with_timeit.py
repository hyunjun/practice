from itertools import product
import numpy as np
import timeit


def dot_product(a, b):
  return sum([v * b[i] for i, v in enumerate(a)])

V = [[1, 2, 0, 3], [1, 1, 1, 0], [0, 1, 1, 0], [3, 0, 0, 0]]
Va = map(np.array, V)

loops = [(i, j) for i, j in product(range(len(V)), range(len(V))) if i < j]

for i, j in loops:
  print '[{}][{}]\t{}\t{}'.format(i, j, dot_product(V[i], V[j]), np.dot(Va[i], Va[j]))


def foo(loops, V):
  return [dot_product(V[i], V[j]) for i, j in loops]


def bar(loops, V):
  return [np.dot(V[i], V[j]) for i, j in loops]

print timeit.timeit("foo(loops, V)", setup="from __main__ import foo, loops, V")
print timeit.timeit("bar(loops, Va)", setup="from __main__ import bar, loops, Va")
