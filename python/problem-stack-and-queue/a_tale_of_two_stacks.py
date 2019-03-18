#   https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks


#   timeout
class MyQueue0:
    def __init__(self):
        self.stack1, self.stack2 = [], []
        self.peekVal = None

    def peek(self):
        return self.peekVal

    def pop(self):
        if 0 == len(self.stack1):
            return None
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        ret = self.stack2.pop()
        if 0 < len(self.stack2):
            self.peekVal = self.stack2[-1]
        else:
            self.peekVal = None
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return ret

    def put(self, value):
        if 0 == len(self.stack1):
            self.peekVal = value
        self.stack1.append(value)


#   timeout
class MyQueue1:
    def __init__(self):
        self.nStack, self.rStack = [], []
        self.peekVal = None

    def peek(self):
        return self.peekVal

    def pop(self):
        if 0 == len(self.nStack) and 0 == len(self.rStack):
            return None
        while self.nStack:
            self.rStack.append(self.nStack.pop())
        ret = self.rStack.pop()
        if 0 < len(self.rStack):
            self.peekVal = self.rStack[-1]
        else:
            self.peekVal = None
        return ret

    def put(self, value):
        if 0 == len(self.nStack):
            if 0 == len(self.rStack):
                self.peekVal = value
            else:
                self.peekVal = self.rStack[-1]
                while self.rStack:
                    self.nStack.append(self.rStack.pop())
        self.nStack.append(value)


class MyQueue:
    def __init__(self):
        self.stack1, self.stack2 = [], []
    
    def move(self):
        if 0 == len(self.stack2):
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def peek(self):
        self.move()
        return self.stack2[-1]
        
    def pop(self):
        self.move()
        return self.stack2.pop()
        
    def put(self, value):
        self.stack1.append(value)
