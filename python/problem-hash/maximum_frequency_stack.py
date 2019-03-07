#   https://leetcode.com/problems/maximum-frequency-stack

#   https://leetcode.com/problems/maximum-frequency-stack/solution


#   Time Limit Exceeded
class FreqStack0(object):

    def __init__(self):
        self.lastNum, self.counter, self.indices = 0, {}, {}

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x in self.counter:
            self.counter[x] += 1
            self.indices[x].append(self.lastNum)
        else:
            self.counter[x] = 1
            self.indices[x] = [self.lastNum]
        self.lastNum += 1

    def pop(self):
        """
        :rtype: int
        """
        if sum(self.counter.values()) <= 0:
            return None
        maxIdxVal, maxIdx, maxCnt = None, 0, max(self.counter.values())
        print(self.counter, self.indices, self.lastNum, maxCnt)
        for c, cnt in self.counter.items():
            if cnt == maxCnt:
                if maxIdx <= self.indices[c][-1]:
                    maxIdxVal, maxIdx = c, self.indices[c][-1]
        print('max cnt {}, max idx {}, max idx value {}'.format(maxCnt, maxIdx, maxIdxVal))
        self.counter[maxIdxVal] -= 1
        self.indices[maxIdxVal].pop()
        return maxIdxVal

from collections import defaultdict

#   runtime; 11160ms, 5.16%
#   memory; 19.4MB, 10.00%
class FreqStack:

    def __init__(self):
        self.maxCnt, self.counter, self.indices = 0, defaultdict(int), defaultdict(list)

    def push(self, x):
        self.counter[x] += 1
        self.maxCnt = max(self.maxCnt, self.counter[x])
        self.indices[self.counter[x]].append(x)

    def pop(self):
        if set(self.counter.values()) == set([0]):
            return None
        num = self.indices[self.maxCnt].pop()
        self.counter[num] -= 1
        #print(self.maxCnt - 1, self.counter.values())
        self.maxCnt = max(self.maxCnt - 1, max(self.counter.values()))
        #print(self.counter, self.indices, self.maxCnt)
        return num


# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
print(5 == obj.pop())
print(7 == obj.pop())
print(5 == obj.pop())
print(4 == obj.pop())

obj = FreqStack()
obj.push(4)
obj.push(0)
obj.push(9)
obj.push(3)
obj.push(4)
obj.push(2)
print(4 == obj.pop())
obj.push(6)
print(6 == obj.pop())
obj.push(1)
print(1 == obj.pop())
obj.push(1)
print(1 == obj.pop())
obj.push(4)
print(4 == obj.pop())
print(2 == obj.pop())
print(3 == obj.pop())
print(9 == obj.pop())
print(0 == obj.pop())
print(4 == obj.pop())
