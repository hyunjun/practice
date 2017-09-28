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


# 위와 동일하지만 간단하게 바꾼 코드
# bin(<int>)는 string type의 binary number를 반환하므로
#   e.g. bin(6) == '0b110'
#   앞의 0b를 제거하고 bin(6)[2:] = '110'
#   이 값을 뒤집어서 bin(6)[2:][::-1] = '011'
#   1인 위치의 index만 가져오면 [1, 2]
def indices2(n):
  result = []
  for i in range(pow(2, n)):
    result.append([idx for idx, c in enumerate(bin(i)[2:][::-1]) if c == '1'])
  return result


arr = ['a', 'b', 'c']
for a in indices(len(arr)):
  print([arr[i] for i in a])
  #print map(lambda t: arr[t], a)
for a in indices2(len(arr)):
  print([arr[i] for i in a])
