#   https://www.hackerrank.com/challenges/qheap1


#   Timeout for 3/18 test cases
class MinHeap0:
    def __init__(self):
        self.heap = [None]

    def add(self, val):
        self.heap.append(val)
        pos = len(self.heap) - 1
        while 1 < pos:
            pPos = int(pos // 2)
            if self.heap[pPos] < self.heap[pos]:
                break
            self.heap[pPos], self.heap[pos] = self.heap[pos], self.heap[pPos]
            pos = pPos
        print(self.heap)

    def delete(self, val):
        tmp = []
        while 1 < len(self.heap) and self.heap[1] != val:
            tmp.append(self.pop())
        if 1 < len(self.heap) and self.heap[1] == val:
            self.pop()
        for t in tmp:
            self.add(t)

    def pop(self):
        if len(self.heap) < 2:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        ret = self.heap[1]
        self.heap[1] = self.heap.pop()
        pos = 1
        while pos < len(self.heap):
            cPos = 2 * pos
            if len(self.heap) <= cPos:
                break
            if cPos + 1 < len(self.heap) and self.heap[cPos] > self.heap[cPos + 1]:
                cPos += 1
            self.heap[pos], self.heap[cPos] = self.heap[cPos], self.heap[pos]
            pos = cPos
        return ret
            
    def print(self):
        if 1 < len(self.heap):
            print(self.heap[1])


#   Timeout for 2/18 test cases
class MinHeap1:
    def __init__(self):
        self.heap = [None]

    def add(self, val):
        self.heap.append(val)
        pos = len(self.heap) - 1
        while 1 < pos:
            pPos = int(pos // 2)
            if self.heap[pPos] < self.heap[pos]:
                break
            self.heap[pPos], self.heap[pos] = self.heap[pos], self.heap[pPos]
            pos = pPos
        print(self.heap)

    def delete(self, val):
        if len(self.heap) < 2:
            return
        q = [1]
        while q:
            pos = q.pop(0)
            if val == self.heap[pos]:
                break
            if self.heap[pos] < val:
                if pos * 2 < len(self.heap):
                    q.append(pos * 2)
                if pos * 2 + 1 < len(self.heap):
                    q.append(pos * 2 + 1)
        if pos == len(self.heap) - 1:
            self.heap.pop()
            return
        self.heap[pos] = self.heap.pop()
        while pos < len(self.heap):
            cPos = 2 * pos
            if len(self.heap) <= cPos:
                break
            if cPos + 1 < len(self.heap) and self.heap[cPos] > self.heap[cPos + 1]:
                cPos += 1
            self.heap[pos], self.heap[cPos] = self.heap[cPos], self.heap[pos]
            pos = cPos
            
    def print(self):
        if 1 < len(self.heap):
            print(self.heap[1])


import heapq


#   Timeout for 2/18 test cases
class MinHeap2:
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        print(self.heap)

    def delete(self, val):
        if len(self.heap) < 1:
            return
        tmp = []
        while self.heap[0] != val:
            tmp.append(heapq.heappop(self.heap))
        heapq.heappop(self.heap)
        for t in tmp:
            heapq.heappush(self.heap, t)
        print(self.heap)
            
    def print(self):
        if 0 < len(self.heap):
            print(self.heap[0])


class MinHeap:
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)

    def delete(self, val):
        if len(self.heap) < 1:
            return
        idx = self.heap.index(val)
        if 1 == len(self.heap) or idx == len(self.heap) - 1:
            self.heap.pop()
        else:
            self.heap[idx] = self.heap.pop()
            heapq.heapify(self.heap)
            
    def print(self):
        if 0 < len(self.heap):
            print(self.heap[0])


s = MinHeap()
N = int(input())
while 0 < N:
    N -= 1
    cmds = input()
    if ' ' in cmds:
        cmd, param = cmds.split(' ')
    else:
        cmd = cmds
    if '1' == cmd:
        s.add(int(param))
    elif '2' == cmd:
        s.delete(int(param))
    elif '3' == cmd:
        s.print()
