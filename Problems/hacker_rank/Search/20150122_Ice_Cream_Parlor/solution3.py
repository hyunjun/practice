def flavor_index(flavors, money):
  for i in range(len(flavors) - 1):
    for j in range(i + 1, len(flavors)):
      if flavors[i] + flavors[j] == money:
        return [i + 1, j + 1]
  return []

if __name__ == '__main__':
  for t in range(int(input())):
    money = int(input())
    int(input())
    print(' '.join([str(i) for i in flavor_index([int(i) for i in input().split()], money)]))
