#   https://www.hackerrank.com/challenges/maximum-element


class MaxStack:
    def __init__(self):
        self.stack1, self.stack2 = [], []

    def push(self, val):
        self.stack1.append(val)
        if 0 == len(self.stack2):
            self.stack2.append(val)
        else:
            self.stack2.append(max(self.stack2[-1], val))

    def pop(self):
        if 0 < len(self.stack1):
            self.stack1.pop()
            self.stack2.pop()

    def print(self):
        if 0 < len(self.stack2):
            print(self.stack2[-1])

s = MaxStack()
N = int(input())
while 0 < N:
    N -= 1
    cmds = input()
    if ' ' in cmds:
        cmd, param = cmds.split(' ')
    else:
        cmd = cmds
    if '1' == cmd:
        s.push(int(param))
    elif '2' == cmd:
        s.pop()
    elif '3' == cmd:
        s.print()
