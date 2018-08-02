#   https://leetcode.com/problems/design-hashmap


#   29.29%
class MyHashMap:
    def __init__(self):
        self.s = [-1] * 1000001
    def put(self, key, value):
        self.s[key] = value
    def get(self, key):
        return self.s[key]
    def remove(self, key):
        self.s[key] = -1


hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
print(1 == hashMap.get(1))
print(-1 == hashMap.get(3))
hashMap.put(2, 1)
print(1 == hashMap.get(2))
hashMap.remove(2)
print(-1 == hashMap.get(2))
