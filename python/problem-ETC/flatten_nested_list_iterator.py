#   https://leetcode.com/problems/flatten-nested-list-iterator


'''
class NestedIterator(object):

    def __init__(self, nestedList):
        self.l = nestedList

    def next(self):
        while self.hasNext():
            item = self.l.pop(0)
            if isinstance(item, list):
                ret = item.pop(0)
                while item:
                    self.l.insert(0, item.pop())
                return ret
            return item
        return None

    def hasNext(self):
        if self.l is not None and 0 < len(self.l):
            return True
        return False
'''

class NestedIterator(object):

    def __init__(self, nestedList):
        self.l = self._flatten(nestedList)

    def _flatten(self, arr):
        r = []
        for i in arr:
            if isinstance(i, list):
                r.extend(self._flatten(i))
            else:
                r.append(i)
        return r

    def next(self):
        while self.hasNext():
            return self.l.pop(0)
        return None

    def hasNext(self):
        if self.l is not None and 0 < len(self.l):
            return True
        return False

'''
#   위와 똑같은 코드이지만, 해당 문제의 NestedInteger class를 이용하는 코드
#   이걸 써야 leetcode에 제출 가능
#   runtime; 80ms, 23.34%
#   memory; 17.5MB, 41.94%
class NestedIterator(object):

    def __init__(self, nestedList):
        self.l = self._flatten(nestedList)

    def _flatten(self, arr):
        r = []
        for i in arr:
            #if isinstance(i, list):
            if False == i.isInteger():
                r.extend(self._flatten(i.getList()))
            else:
                r.append(i.getInteger())
        return r

    def next(self):
        while self.hasNext():
            return self.l.pop(0)
        return None

    def hasNext(self):
        if self.l is not None and 0 < len(self.l):
            return True
        return False
'''

data = [([[1,1],2,[1,1]], [1,1,2,1,1]),
        ([1,[4,[6]]], [1,4,6]),
        ]
for inp, expected in data:
    ni = NestedIterator(inp)
    real = []
    while ni.hasNext():
        real.append(ni.next())
    print(f'{inp}, expected {expected}, real {real}, result {expected == real}')
