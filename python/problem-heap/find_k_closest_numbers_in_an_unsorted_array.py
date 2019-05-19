#   https://www.geeksforgeeks.org/find-k-closest-numbers-in-an-unsorted-array


class MaxHeap:
    def __init__(self):
        self.heap = [None]

    def isEmpty(self):
        if 1 == len(self.heap):
            return True
        return False

    def size(self):
        return len(self.heap) - 1

    def peek(self):
        if self.isEmpty():
            return None
        return self.heap[1]

    def swap(self, i, j):
        if not self.isEmpty() and 0 < i < len(self.heap) and 0 < j < len(self.heap):
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def push(self, diff, val):
        self.heap.append((diff, val))
        idx = len(self.heap) - 1
        while 1 < idx:
            pIdx = idx // 2
            if self.heap[pIdx][0] >= self.heap[idx][0]:
                break
            self.swap(pIdx, idx)
            idx = pIdx

    def pop(self):
        if self.isEmpty():
            return None
        if 1 == self.size():
            return self.heap.pop()
        ret = self.heap[1]
        self.heap[1] = self.heap.pop()
        idx = 1
        while idx < len(self.heap):
            tIdx, lIdx, rIdx = idx, 2 * idx, 2 * idx + 1
            if lIdx < len(self.heap) and self.heap[tIdx][0] < self.heap[lIdx][0]:
                tIdx = lIdx
            if rIdx < len(self.heap) and self.heap[tIdx][0] < self.heap[rIdx][0]:
                tIdx = rItdx
            if idx == tIdx:
                break
            self.swap(idx, tIdx)
            idx = tIdx
        return ret


def find_k_closest(arr, x, k):
    if arr is None or 0 == len(arr):
        return []
    if len(arr) <= k:
        return arr

    heap = MaxHeap()
    for a in arr:
        if heap.size() >= k:
            if abs(x - a) >= heap.peek()[0]:
                continue
            heap.pop()
        heap.push(abs(x - a), a)

    res = []
    while not heap.isEmpty():
        res.append(heap.pop()[1])
    return res


data = [([10, 2, 14, 4, 7, 6], 5, 3, [4, 6, 7]),
        ([-10, -50, 20, 17, 80], 20, 2, [17, 20]),
        ]
for arr, x, k, expected in data:
    real = find_k_closest(arr, x, k)
    print('{}, {}, {}, expected {}, real {}, result {}'.format(arr, x, k, expected, real, sorted(expected) == sorted(real)))
