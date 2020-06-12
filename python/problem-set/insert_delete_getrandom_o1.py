#   https://leetcode.com/problems/insert-delete-getrandom-o1


#   Wrong Answer
class RandomizedSet0:
    def __init__(self):
        self.i, self.d, self.l = 0, {}, []
        
    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = self.i
        self.l.insert(self.i, val)
        self.i += 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.d:
            idx = self.d[val]
            del self.d[val]
            self.l[idx] = None
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.l)


#   https://leetcode.com/submissions/detail/352620575/?from=/explore/featured/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3358
#   runtime; 100ms, 83.81%
#   memory; 17.9MB
class RandomizedSet:
    def __init__(self):
        self.i, self.d, self.l = 0, {}, []
        
    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = self.i
        self.l.insert(self.i, val)
        self.i += 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.d:
            idx = self.d[val]
            del self.d[val]
            self.l[idx] = None
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.l)
