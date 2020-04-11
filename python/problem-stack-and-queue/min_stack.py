#   https://leetcode.com/problems/min-stack


import sys


#   76.79%
class MinStack0(object):

    def __init__(self):
        self.stack = []
        self.minValues = []

    def push(self, x):
        self.stack.append(x)
        if 0 == len(self.minValues) or x < self.minValues[-1]:
            self.minValues.append(x)
        else:
            self.minValues.append(self.minValues[-1])

    def pop(self):
        if 0 < len(self.stack):
            self.stack.pop()
            self.minValues.pop()

    def top(self):
        if 0 < len(self.stack):
            return self.stack[-1]
        return -sys.maxsize

    def getMin(self):
        if 0 < len(self.minValues):
            return self.minValues[-1]
        return -sys.maxsize


#   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3292
#   runtime; 60ms, 77.04%
#   memory; 17.6MB
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []

    def push(self, x: int) -> None:
        if 0 < len(self.stack):
            self.mins.append(min(self.mins[-1], x))
        else:
            self.mins.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        if 0 < len(self.stack):
            self.stack.pop()
            self.mins.pop()

    def top(self) -> int:
        if 0 < len(self.stack):
            return self.stack[-1]
        return None
        
    def getMin(self) -> int:
        if 0 < len(self.stack):
            return self.mins[-1]
        return None


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin() == -3)
minStack.pop()
print(minStack.top() == 0)
print(minStack.getMin() == -2)
