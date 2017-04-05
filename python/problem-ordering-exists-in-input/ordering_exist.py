# https://www.careercup.com/question?id=5659201272545280

def has_ordering(inp, ord):
  d = {}
  for i, c in enumerate(inp):
    d[c] = i
  prev = d[ord[0]]
  for c in ord:
    cur = d[c]
    if prev > cur:
      return False
    prev = cur
  return True

# the first expected result is False because all Ls are not before all Os
data = [('hello world!', 'hlo!', False), ('hello world!', '!od', False), ('hello world!', 'he!', True), ('aaaabbbbbcccccc', 'ac', True)]
for inp, ord, expected_result in data:
  print inp, ord, expected_result, has_ordering(inp, ord)
