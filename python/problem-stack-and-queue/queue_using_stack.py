#   https://leetcode.com/problems/implement-queue-using-stacks
#   94.71%

#   https://leetcode.com/problems/implement-queue-using-stacks/solution

import sys


class MyQueue:

    def __init__(self):
        self.stack, self.tmpStack = [], []

    def push(self, x):
        while self.stack:
            self.tmpStack.append(self.stack.pop())
        self.stack.append(x)
        while self.tmpStack:
            self.stack.append(self.tmpStack.pop())
        print(self.stack)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return -sys.maxsize

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return -sys.maxsize

    def empty(self):
        if self.stack:
            return False
        return True


myQueue = MyQueue()
myQueue.push(-2)
myQueue.push(0)
myQueue.push(-3)
print(myQueue.pop() == -2)
print(myQueue.peek() == 0)
print(False == myQueue.empty())
myQueue.push(3)
print(myQueue.pop() == 0)
print(myQueue.pop() == -3)
print(myQueue.pop() == 3)
print(True == myQueue.empty())
