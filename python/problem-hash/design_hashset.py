#   https://leetcode.com/problems/design-hashset


#   46.62%
class MyHashSet:
    def __init__(self):
        self.s = [False] * 1000001
    def add(self, key):
        self.s[key] = True
    def remove(self, key):
        self.s[key] = False
    def contains(self, key):
        return self.s[key]


hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
print(True == hashSet.contains(1))
print(False == hashSet.contains(3))
hashSet.add(2)
print(True == hashSet.contains(2))
hashSet.remove(2)
print(False == hashSet.contains(2))
