def fact(n):
  def _fact(prod, n):
    if n == 1:
      return prod
    return _fact(prod * n, n - 1)
  return _fact(1, n)

def sin(x):
  return x - x**3 / fact(3) + x**5 / fact(5) - x**7 / fact(7) + x**9 / fact(9)

def cos(x):
  return 1 - x**2 / fact(2) + x**4 / fact(4) - x**6 / fact(6) + x**8 / fact(8)

if __name__ == '__main__':
  N = int(raw_input())
  for i in range(N):
    x = float(raw_input())
    print sin(x)
    print cos(x)
