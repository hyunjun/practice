from itertools import islice


# https://mingrammer.com/translation-iterators-vs-generators
def fib():
  prev, curr = 0, 1
  while True:
    yield curr
    prev, curr = curr, prev + curr


f = fib()
print list(islice(f, 0, 10))
