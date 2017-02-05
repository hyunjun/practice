# https://www.interviewcake.com/question/python/highest-product-of-3
def highest_product(arr):
  a, b, c = arr[0], arr[1], arr[2]
  ab, ac, bc = a * b, a * c, b * c
  abc = a * b * c
  for i in range(3, len(arr)):
    _a, _b, _c = arr[i - 2], arr[i - 1], arr[i]
    a, b, c = max(a, _a), max(b, _b), max(c, _c)
    ab, ac, bc = max(ab, _a * _b), max(ac, _a * _c), max(bc, _b * _c)
    abc = max(abc, _a * _b * _c)
  return max([a, b, c, ab, ac, bc, abc])

print highest_product([-10, -10, 3])
print highest_product([1, 200, 0, -10, -10, 3])
