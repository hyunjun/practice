from itertools import islice


# https://mingrammer.com/translation-iterators-vs-generators
def fib():
  prev, curr = 0, 1
  while True:
    yield curr
    prev, curr = curr, prev + curr


f = fib()
print(list(islice(f, 0, 10)))

#   yield를 사용하는 또 다른 방법
f = fib()
try:
    for _ in range(10):
        print(next(f))
except StopIteration as e:
    print(e)
