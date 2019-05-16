#   https://aonecode.com/amazon-online-assessment-questions Q3


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

    def push(self, val):
        self.heap.append(val)
        idx = len(self.heap) - 1
        while 1 < idx:
            pIdx = idx // 2
            if self.heap[pIdx][0] < self.heap[idx][0]:
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
            tIdx, lIdx, rIdx = idx, idx * 2, idx * 2 + 1
            if lIdx < len(self.heap) and self.heap[tIdx][0] < self.heap[lIdx][0]:
                tIdx = lIdx
            if rIdx < len(self.heap) and self.heap[tIdx][0] < self.heap[rIdx][0]:
                tIdx = rIdx
            if tIdx == idx:
                break
            self.swap(tIdx, idx)
            idx = tIdx
        return ret


def k_nearest_post_offices(start, post_offices, k):
    if post_offices is None or 0 == len(post_offices):
        return []
    if len(post_offices) <= k:
        return post_offices
    max_heap = MaxHeap()
    for post_office in post_offices:
        dist = (start[0] - post_office[0]) ** 2 + (start[1] - post_office[1]) ** 2
        if max_heap.size() == k and max_heap.peek()[0] <= dist:
            continue
        if max_heap.size() == k:
            max_heap.pop()
        max_heap.push([dist, post_office])
    res = []
    while not max_heap.isEmpty():
        res.append(max_heap.pop()[1])
    return res


data = [([0, 0], [[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]], 3, [[-1, 2], [0, 3], [4, 3]]),
        ]
for start, post_offices, k, expected in data:
    real = k_nearest_post_offices(start, post_offices, k)
    print('{}, {}, {}, expected {}, real {}, result {}'.format(start, post_offices, k, expected, real, sorted(expected) == sorted(real)))
