#   https://www.hackerrank.com/challenges/find-the-running-median


class Heap:
    def __init__(self, _cmp):
        self.heap = [None]
        self._cmp = _cmp

    def isEmpty(self):
        if 1 == len(self.heap):
            return True
        return False

    def peek(self):
        if self.isEmpty():
            return None
        return self.heap[1]

    def swap(self, idx1, idx2):
        if idx1 < len(self.heap) and idx2 < len(self.heap):
            self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def add(self, val):
        self.heap.append(val)
        idx = len(self.heap) - 1
        while 1 < idx:
            pIdx = idx // 2
            print(self.heap, pIdx, idx)
            if 1 <= pIdx and self._cmp(self.heap[pIdx], self.heap[idx]):
                self.swap(pIdx, idx)
            idx = pIdx

    def remove(self):
        if self.isEmpty():
            return None
        self.swap(1, len(self.heap) - 1)
        ret = self.heap.pop()
        if not self.isEmpty():
            idx = 1
            while idx < len(self.heap):
                tIdx, lIdx, rIdx = idx, 2 * idx, 2 * idx + 1
                if lIdx < len(self.heap) and self._cmp(self.heap[idx], self.heap[lIdx]):
                    tIdx = lIdx
                if rIdx < len(self.heap) and self._cmp(self.heap[tIdx], self.heap[rIdx]):
                    tIdx = rIdx
                if idx == tIdx:
                    break
                self.swap(idx, tIdx)
                idx = tIdx
        return ret


import operator


class MinHeap(Heap):
    def __init__(self):
        #Heap.__init__(self, operator.gt)
        Heap.__init__(self, lambda a, b: a > b)

    '''
    def add(self, val):
        Heap.add(self, val, operator.gt)
        #self.heap.append(val)
        #idx = len(self.heap) - 1
        #while 1 < idx:
        #    pIdx = idx // 2
        #    if 1 <= pIdx and self.heap[pIdx] > self.heap[idx]:
        #        self.swap(pIdx, idx)
        #    idx = pIdx

    def remove(self):
        return Heap.remove(self, operator.gt)
        #if self.isEmpty():
        #    return None
        #self.swap(1, len(self.heap) - 1)
        #ret = self.heap.pop()
        #if not self.isEmpty():
        #    idx = 1
        #    while idx < len(self.heap):
        #        tIdx, lIdx, rIdx = idx, 2 * idx, 2 * idx + 1
        #        if lIdx < len(self.heap) and self.heap[idx] > self.heap[lIdx]:
        #            tIdx = lIdx
        #        if rIdx < len(self.heap) and self.heap[tIdx] > self.heap[rIdx]:
        #            tIdx = rIdx
        #        if idx == tIdx:
        #            break
        #        self.swap(idx, tIdx)
        #        idx = tIdx
        #return ret
    '''


class MaxHeap(Heap):
    def __init__(self):
        #Heap.__init__(self, operator.lt)
        Heap.__init__(self, lambda a, b: a < b)

    '''
    def add(self, val):
        Heap.add(self, val, operator.lt)
        #self.heap.append(val)
        #idx = len(self.heap) - 1
        #while 1 < idx:
        #    pIdx = idx // 2
        #    if 1 <= pIdx and self.heap[pIdx] < self.heap[idx]:
        #        self.swap(pIdx, idx)
        #    idx = pIdx

    def remove(self):
        return Heap.remove(self, operator.lt)
        #if self.isEmpty():
        #    return None
        #self.swap(1, len(self.heap) - 1)
        #ret = self.heap.pop()
        #if not self.isEmpty():
        #    idx = 1
        #    while idx < len(self.heap):
        #        tIdx, lIdx, rIdx = idx, 2 * idx, 2 * idx + 1
        #        if lIdx < len(self.heap) and self.heap[idx] < self.heap[lIdx]:
        #            tIdx = lIdx
        #        if rIdx < len(self.heap) and self.heap[tIdx] < self.heap[rIdx]:
        #            tIdx = rIdx
        #        if idx == tIdx:
        #            break
        #        self.swap(idx, tIdx)
        #        idx = tIdx
        #return ret
    '''


def runningMedian(a):
    res, median, minHeap, maxHeap = [], 0, MinHeap(), MaxHeap()
    for i, n in enumerate(a):
        #print('max heap {}, min heap {}\tnew item {}'.format(maxHeap.heap, minHeap.heap, n))
        if n <= median:
            maxHeap.add(n)
        else:
            minHeap.add(n)

        if len(minHeap.heap) > len(maxHeap.heap) + 1:
            maxHeap.add(minHeap.remove())
        if len(maxHeap.heap) > len(minHeap.heap) + 1:
            minHeap.add(maxHeap.remove())

        if len(minHeap.heap) == len(maxHeap.heap):
            median = (maxHeap.peek() + minHeap.peek()) / 2
        elif len(minHeap.heap) > len(maxHeap.heap):
            median = float(minHeap.peek())
        elif len(minHeap.heap) < len(maxHeap.heap):
            median = float(maxHeap.peek())
        res.append(median)

        #   Wrong Answer
        #minHeap.add(n)
        #if 0 == i % 2:
        #    res.append(float(minHeap.peek()))
        #else:
        #    if not minHeap.isEmpty():
        #        maxHeap.add(minHeap.remove())
        #    res.append((minHeap.peek() + maxHeap.peek()) / 2)
    return res


data = [([12, 4, 5, 3, 8, 7], [12.0, 8.0, 5.0, 4.5, 5.0, 6.0]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]),
        ([5, 15, 1, 3], [5, 10, 5, 4]),
        ([1, 2, 3], [1, 1.5, 2]),
        ]
for a, expected in data:
    real = runningMedian(a)
    print('{}, expected {}, real {}, result {}'.format(a, expected, real, expected == real))
