#   https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks


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
