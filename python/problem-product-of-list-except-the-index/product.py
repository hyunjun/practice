# https://www.interviewcake.com/question/python/product-of-other-numbers


def product(arr):
  result = [1] * len(arr)
  acc = 1
  for i in range(1, len(arr)):
    acc *= arr[i - 1]
    result[i] *= acc
  acc = 1
  for i in range(len(arr) - 2, -1, -1):
    acc *= arr[i + 1]
    result[i] *= acc
  return result


print(product([1, 7, 3, 4]))
