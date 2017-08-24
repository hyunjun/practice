# https://leetcode.com/problems/add-binary

def add_binary(a, b):
  if (a is None or 0 == len(a)) and (b is None or 0 == len(b)):
    return '0'
  if a is None or 0 == len(a) or '0' == a:
    return b
  if b is None or 0 == len(b) or '0' == b:
    return a

  result, longer, shorter = [], a[::-1], b[::-1]
  if len(a) < len(b):
    longer, shorter = shorter, longer

  transfer = 0
  #print('shorter {}\tlonger {}'.format(shorter, longer))
  for i, c in enumerate(shorter):
    l = [int(c), int(longer[i]), transfer]
    l.sort()
    #print('[{}]\t{}'.format(i, l))
    if l == [0, 0, 0]:
      result.append(0)
      transfer = 0
    elif l == [0, 0, 1]:
      result.append(1)
      transfer = 0
    elif l == [0, 1, 1]:
      result.append(0)
      transfer = 1
    else:
      result.append(1)
      transfer = 1
  #print('[after 1st loop]\tresult {}\ttransfer {}'.format(result, transfer))
  if len(shorter) < len(longer):
    #print('loop from {} to {}'.format(len(shorter), len(longer)))
    for i in range(len(shorter), len(longer)):
      l = [int(longer[i]), transfer]
      l.sort()
      #print('[{}]\t{}'.format(i, l))
      if l == [0, 0]:
        result.append(0)
        transfer = 0
      elif l == [1, 1]:
        result.append(0)
        transfer = 1
      else:
        result.append(1)
        transfer = 0
  if transfer == 1:
    result.append(1)
  #print('[after 2nd loop]\tresult {}\ttransfer {}'.format([c for c in result[::-1]], transfer))
  return str(''.join([str(c) for c in result[::-1]]))

cases = [('11', '1', '100'), ('0', '0', '0'), ('1', '1', '10'), ('111', '1', '1000'), ('1010', '1011', '10101')]
for a, b, expected in cases:
  real = add_binary(a, b)
  print('a = {}\tb = {}\texpected = {}\treal = {}\tresult = {}'.format(a, b, expected, real, expected == real))
