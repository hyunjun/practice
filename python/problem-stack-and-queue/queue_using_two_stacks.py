#   https://www.hackerrank.com/challenges/queue-using-two-stacks


class MyQueue:
    def __init__(self):
        self.stack1, self.stack2 = [], []

    def enqueue(self, val):
        self.stack1.append(val)

    def move(self):
        if 0 == len(self.stack2):
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def dequeue(self):
        self.move()
        if 0 < len(self.stack2):
            return self.stack2.pop()

    def print(self):
        self.move()
        if 0 < len(self.stack2):
            print(self.stack2[-1])

q = MyQueue()
N = int(input())
while 0 < N:
    N -= 1
    cmds = input()
    if ' ' in cmds:
        cmd, param = cmds.split(' ')
    else:
        cmd = cmds
    if '1' == cmd:
        q.enqueue(param)
    elif '2' == cmd:
        q.dequeue()
    elif '3' == cmd:
        q.print()
