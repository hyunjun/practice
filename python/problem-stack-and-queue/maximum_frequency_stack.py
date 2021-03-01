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
class FreqStack1:

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


#   Time Limit Exceeded
class FreqStack2:

    def __init__(self):
        self.stack, self.freq = [], defaultdict(int)

    def push(self, x):
        self.stack.append(x)
        self.freq[x] += 1

    def pop(self):
        freqList = self.freq.items()
        maxCnt = sorted(freqList, key=lambda t: -t[1])[0][1]
        nums = set([i for i, cnt in freqList if cnt == maxCnt])
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] in nums:
                ret = self.stack.pop(i)
                self.freq[ret] -= 1
                break
        return ret


#   https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3655
#   runtime: 4212ms
#   memory: 22.1MB, 91.24%
class FreqStack:

    def __init__(self):
        self.stack, self.maxStack, self.freq = [], [], defaultdict(int)

    def push(self, x):
        self.stack.append(x)
        self.freq[x] += 1
        if 0 == len(self.maxStack) or self.freq[x] >= self.freq[self.maxStack[-1]]:
            self.maxStack.append(x)
        else:
            self.maxStack.append(self.maxStack[-1])

    def pop(self):
        ret = self.maxStack.pop()
        self.freq[ret] -= 1
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == ret:
                self.stack.pop(i)
                break
        maxCnt = max(self.freq.values())
        if 0 < len(self.maxStack) and self.freq[self.maxStack[-1]] <= maxCnt:
            for i in range(len(self.stack) - 1, -1, -1):
                if self.freq[self.stack[i]] == maxCnt:
                    self.maxStack[-1] = self.stack[i]
                    break
        return ret


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
