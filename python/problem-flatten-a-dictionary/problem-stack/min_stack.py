#   https://leetcode.com/problems/min-stack
#   76.79%


import sys


class MinStack(object):

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


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin() == -3)
minStack.pop()
print(minStack.top() == 0)
print(minStack.getMin() == -2)
