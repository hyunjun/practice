#   https://leetcode.com/problems/implement-stack-using-queues
#   95.61%

#   https://leetcode.com/problems/implement-stack-using-queues/solution


import sys


class MyStack:

    def __init__(self):
        self.q1, self.q2 = [], []
        self.isQ1 = True

    def push(self, x):
        if self.isQ1:
            self.q1.append(x)
            if 0 < len(self.q2):
                self.q1.extend(self.q2)
                self.q2 = []
        else:
            self.q2.append(x)
            if 0 < len(self.q1):
                self.q2.extend(self.q1)
                self.q1 = []
        print(self.q1, self.q2)
        self.isQ1 = not self.isQ1

    def pop(self):
        if 0 < len(self.q1):
            ret = self.q1[0]
            del self.q1[0]
        elif 0 < len(self.q2):
            ret = self.q2[0]
            del self.q2[0]
        else:
            ret = -sys.maxsize
        print(self.q1, self.q2)
        return ret

    def top(self):
        if 0 < len(self.q1):
            ret = self.q1[0]
        elif 0 < len(self.q2):
            ret = self.q2[0]
        else:
            ret = -sys.maxsize
        print(self.q1, self.q2)
        return ret

    def empty(self):
        if 0 == len(self.q1) and 0 == len(self.q2):
            return True
        return False


myStack = MyStack()
myStack.push(-2)
myStack.push(0)
myStack.push(-3)
print(myStack.pop() == -3)
print(myStack.top() == 0)
