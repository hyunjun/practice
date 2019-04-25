#   https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

#   https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85296/Shortest-possible-solution-in-Python-(seriously!)


class MaxHeap:
    def __init__(self):
        self.heap = [None]

    def size(self):
        return len(self.heap) - 1

    def peek(self):
        if 0 == self.size():
            return None
        return self.heap[1]

    def swap(self, i, j):
        if max(i, j) < len(self.heap):
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def add(self, val):
        self.heap.append(val)
        idx = len(self.heap) - 1
        while 1 < idx:
            pIdx = idx // 2
            if self.heap[pIdx] < self.heap[idx]:
                self.swap(pIdx, idx)
            idx = pIdx

    def pop(self):
        if 0 == self.size():
            return None
        if 1 == self.size():
            return self.heap.pop()
        ret = self.heap[1]
        self.heap[1] = self.heap.pop()
        idx = 1
        while idx < len(self.heap):
            lIdx, rIdx, tIdx = 2 * idx, 2 * idx + 1, idx
            if lIdx < len(self.heap) and self.heap[lIdx] > self.heap[idx]:
                tIdx = lIdx
            if rIdx < len(self.heap) and self.heap[rIdx] > self.heap[tIdx]:
                tIdx = rIdx
            if tIdx == idx:
                break
            self.swap(tIdx, idx)
            idx = tIdx


class Solution:
    #   runtime; 1928ms, 5.03%
    #   memory; 16.4MB, 91.97%
    def kthSmallest0(self, matrix, k):
        if matrix is None or 0 == len(matrix) or 0 == len(matrix[0]):
            return None
        cnt, val = 0, 0
        while cnt < k:
            minVal, minRow = float('inf'), -1
            for r in range(len(matrix)):
                if 0 < len(matrix[r]) and matrix[r][0] < minVal:
                    minVal, minRow = matrix[r][0], r
            val = matrix[minRow].pop(0)
            cnt += 1
        return val

    #   runtime; 1168ms, 5.03%
    #   memory; 17.6MB, 10.22%
    def kthSmallest(self, matrix, k):
        if matrix is None or 0 == len(matrix) or 0 == len(matrix[0]):
            return None
        heap = MaxHeap()
        for r in range(len(matrix)):
            if k <= heap.size() and heap.peek() < matrix[r][0]:
                break
            for c in range(len(matrix[r])):
                heap.add(matrix[r][c])
        while k < heap.size():
            heap.pop()
        return heap.peek()


s = Solution()
data = [([[1,  5,  9], [10, 11, 13], [12, 13, 15]], 8, 13),
        ([[1,  5,  9], [2, 6, 10], [3, 7, 11]], 6, 7),
        ]
for matrix, k, expected in data:
    for row in matrix:
        print(row)
    real = s.kthSmallest(matrix, k)
    print('{}, expected {}, real {}, result {}'.format(k, expected, real, expected == real))
