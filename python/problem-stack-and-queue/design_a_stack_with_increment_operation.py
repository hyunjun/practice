#   https://leetcode.com/problems/design-a-stack-with-increment-operation


#   runtime; 132ms, 68.48%
#   memory; 14.7MB, 100.00%
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack, self.maxSize = [], maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if 0 < len(self.stack):
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.stack), k)):
            self.stack[i] += val
