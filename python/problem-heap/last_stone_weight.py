#   https://leetcode.com/problems/last-stone-weight


class MaxHeap:
    def __init__(self):
        self.heap = [None]

    def size(self):
        return len(self.heap) - 1

    def isEmpty(self):
        if 0 == self.size():
            return True
        return False

    def swap(self, i, j):
        if not self.isEmpty() and 0 < i < len(self.heap) and 0 < j < len(self.heap):
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def push(self, val):
        self.heap.append(val)
        idx = len(self.heap) - 1
        while 1 < idx:
            pIdx = idx // 2
            if self.heap[pIdx] >= self.heap[idx]:
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
            if lIdx < len(self.heap) and self.heap[tIdx] < self.heap[lIdx]:
                tIdx = lIdx
            if rIdx < len(self.heap) and self.heap[tIdx] < self.heap[rIdx]:
                tIdx = rIdx
            if idx == tIdx:
                break
            self.swap(idx, tIdx)
            idx = tIdx
        return ret


class Solution:
    #   runtime; 44ms, 9.04%
    #   memory; 13.2MB, 100.00%
    def lastStoneWeight0(self, stones):
        if stones is None or 0 == len(stones):
            return 0
        heap = MaxHeap()
        for s in stones:
            heap.push(s)
        while 1 < heap.size():
            a, b = heap.pop(), heap.pop()
            if a > b:
                heap.push(a - b)
        if heap.isEmpty():
            return 0
        return heap.pop()

    #   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3297
    #   runtime; 32ms, 40.92%
    #   memory; 14MB
    def lastStoneWeight(self, stones):
        if stones is None or 0 == len(stones):
            return 0
        while len(stones) > 1:
            arr = sorted(stones)
            a, b = arr.pop(), arr.pop()
            if a > b:
                arr.append(a - b)
            else:
                arr.append(0)
            stones = arr
        return stones[0]


s = Solution()
data = [([2, 7, 4, 1, 8, 1], 1),
        ([2, 2], 0),
        ]
for stones, expected in data:
    real = s.lastStoneWeight(stones)
    print('{}, expected {}, real {}, result {}'.format(stones, expected, real, expected == real))
