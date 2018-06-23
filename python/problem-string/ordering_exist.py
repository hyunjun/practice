# https://www.careercup.com/question?id=5659201272545280


def has_ordering(inp, order):
  d = {}
  for i, c in enumerate(inp):
    d[c] = i
  prev = d[order[0]]
  for c in order:
    cur = d[c]
    if prev > cur:
      return False
    prev = cur
  return True


# the first expected result is False because all Ls are not before all Os
data = [('hello world!', 'hlo!', False), ('hello world!', '!od', False), ('hello world!', 'he!', True), ('aaaabbbbbcccccc', 'ac', True)]
for inp, order, expected_result in data:
  print(inp, order, expected_result, has_ordering(inp, order))
