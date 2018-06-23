'''
Using any language of your choice, write a function that takes an integer argument,
and returns true if the integer is the sum of the squares of two integers, and false otherwise.
(Note that the integer 0 doesn't count).
Example: f(34) = true because 34 = 3*3 + 5*5; f(35) = false
Hint: brute force: O(n^2), optimal: O(n)
'''
import math


def is_sum_of_two_squares(a):
  start = math.sqrt(a)
  if int(start) == start:
    start = int(start) - 1
  else:
    start = int(start)
  for i in range(start, 1, -1):
    rest = a - i * i
    sqrt_rest = math.sqrt(rest)
    if int(sqrt_rest) == sqrt_rest and i != sqrt_rest:
      return True
  return False


for num in [25, 17, 32, 34, 35]:
  print(num, is_sum_of_two_squares(num))
