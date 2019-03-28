#   https://www.hackerrank.com/challenges/jesse-and-cookies


class MyHeap:
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


#   Wrong Answer for 22/28 test cases
def cookies0(k, A):
    heap = MyHeap()
    for a in A:
        if k <= a:
            continue
        heap.add(a)
    cnt = 0
    while 2 < len(heap.heap) and heap.heap[1] < k:
        newCookie = heap.pop() + 2 * heap.pop()
        if newCookie < k:
            heap.add(newCookie)
        cnt += 1
    return cnt


import heapq


#   Wrong Answer for 12/28 test cases
def cookies1(k, A):
    arr = [a for a in sorted(A) if a < k]
    if len(arr) < 2:
        return -1
    heapq.heapify(arr)
    cnt = 0
    while 0 < len(arr):
        if 1 == len(arr):
            return -1
        n = heapq.heappop(arr) + heapq.heappop(arr) * 2
        if n < k:
            heapq.heappush(arr, n)
        cnt += 1
    return cnt


def cookies(k, A):
    if 0 == len(A) or A is None:
        return -1
    heapq.heapify(A)
    cnt = 0
    while 1 < len(A) and A[0] < k:
        heapq.heappush(A, heapq.heappop(A) + heapq.heappop(A) * 2)
        cnt += 1
    if A[0] < k:
        return -1
    return cnt


data = [(7, [1, 2, 3, 9, 10, 12], 2),
        ]
for k, A, expected in data:
    real = cookies(k, A)
    print('{}, {}, expected {}, real {}, result {}'.format(k, A, expected, real, expected == real))
