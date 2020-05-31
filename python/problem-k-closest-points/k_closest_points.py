#   https://leetcode.com/problems/k-closest-points-to-origin/


from typing import List
import math


#   https://www.youtube.com/watch?v=eaYX0Ee0Kcg
def k_closest_point(points, k):
    points.sort(key=lambda t: math.sqrt(t[0] * t[0] + t[1] * t[1]))
    return points[:k]


class MaxHeap:
    def __init__(self):
        self.heap = [None]

    def size(self):
        return len(self.heap) - 1

    def swap(self, i, j):
        l = len(self.heap)
        if i < l and j < l:
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def push(self, info):
        self.heap.append((info[0], info[1]))
        idx = len(self.heap) - 1
        while 1 < idx:
            pIdx = idx // 2
            if self.heap[pIdx][0] < self.heap[idx][0]:
                self.swap(pIdx, idx)
            idx = pIdx

    def peek(self):
        return self.heap[-1]

    def pop(self):
        if 0 == self.size():
            return None
        if 1 == self.size():
            return self.heap.pop()
        ret = self.heap[1]
        self.heap[1] = self.heap.pop()
        idx = 1
        while idx < len(self.heap):
            tIdx, rIdx = 2 * idx, 2 * idx + 1
            if rIdx < len(self.heap) and self.heap[tIdx][0] < self.heap[rIdx][0]:
                tIdx = rIdx
            if tIdx < len(self.heap) and self.heap[idx][0] < self.heap[tIdx][0]:
                self.swap(idx, tIdx)
                idx = tIdx
            else:
                break
        return ret


class Solution:
    def kClosest0(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda t: t[0] ** 2 + t[1] ** 2)[:K]

    #   runtime; 2228ms, 5.09%
    #   memory; 19.4MB, 5.80%
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        maxHeap = MaxHeap()
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            maxHeap.push((dist, point))
            if K < maxHeap.size():
                maxHeap.pop()
        ret = []
        while 0 < maxHeap.size():
            ret.append(maxHeap.pop()[1])
        return ret[::-1]


s = Solution()
data = [([(-2, 4), (0, -2), (-1, 0), (3, 5), (-2, -3), (3, 2)], 3, [(-1, 0), (0, -2), (-2, -3)]),
        ]
for points, K, expect in data:
    real1, real2 = k_closest_point(points, 3), s.kClosest(points, K)
    print(f'{points} expect {expect} real {real1} {real2} result {expect == real1 == real2}')
