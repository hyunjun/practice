def indices(n):
  result = []
  for i in range(pow(2, n)):
    j, index, indice = i, 0, []
    while j > 0:
      if j & 0x1 == 1:
        indice.append(index)
      j >>= 1
      index += 1
    result.append(indice)
  return result

arr = ['a', 'b', 'c']
for a in indices(len(arr)):
  # for i in a:
  #   print arr[i],
  # print
  print map(lambda t: arr[t], a)
