'''
A child is running up a staircase with n steps, and can hop either 1 step, 2
steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the
stairs.
Tip:
  There are three approaches to this problem.
- recursive algorithm
- top-down dynamic programming - it is actually a recursive algorithm with
    caching, that saves repeated sub-problems solutions so there are no
    repetitive calculations.
- bottom-up dynamic programming - starting from the smallest possible
    problem size, and work the way up to the original size problem. This can
    be done by caching states in the table, represented in a 1d or 2d
    arrays. HINT: use two for-loops. The first for-loop is the step size,
    start from 0 to n steps (thus bottom-up). The second for-loop controls
    how many hops a child can start with, which are 1 step, 2 steps, or 3
    steps.
'''

def step_count(n):
  if n == 0:
    return 1
  if n >= 3:
    return step_count(n - 3) + step_count(n - 2) + step_count(n - 1)
  if n >= 2:
    return step_count(n - 2) + step_count(n - 1)
  if n >= 1:
    return step_count(n - 1)

def step_count_general(k, n):
  if n < 0:
    return 0
  if n == 0:
    return 1

  return sum([step_count_general(k, n - i) for i in range(1, k + 1)])

print step_count(4), step_count_general(3, 4)
