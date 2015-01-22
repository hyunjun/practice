'''def flavor_index(flavors, money):
  for i in range(len(flavors) - 1):
    for j in range(i + 1, len(flavors)):
      if flavors[i] + flavors[j] == money:
        return [i + 1, j + 1]
  return []'''

from itertools import chain
from itertools import product

def flavor_index(flavors, money):
  indices = range(0, len(flavors))
  return map(lambda z: map(lambda w: w + 1, z),
             filter(lambda y: flavors[y[0]] + flavors[y[1]] == money,
                    list(chain.from_iterable(map(lambda x: list(product([x], range(x + 1, len(indices)))), indices)))))[0]

if __name__ == '__main__':
  for t in range(int(raw_input())):
    money = int(raw_input())
    int(raw_input())
    print ' '.join([str(i) for i in flavor_index([int(i) for i in raw_input().split()], money)])
