#   https://leetcode.com/problems/find-k-pairs-with-smallest-sums

#   Test code 실행 시 c++ 관련 오류가 발생하면서 실행 불가능
#   MinHeap 사용 여부와는 무관하게 발생
#   Line 31: Char 58: error: conversion from 'vector<std::pair<int, int>>' to non-scalar type 'vector<std::vector<int>>' requested

#   https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/289187/python-O(k%2B(m%2Bn)*log(max_sum))-~-O(n)-by-find-the-kth-sum-99.9


from itertools import product


class MinHeap:
    def __init__(self):
        self.heap = [None]

    def size(self):
        return len(self.heap) - 1

    def isEmpty(self):
        return self.size() == 0

    def swap(self, i, j):
        if not self.isEmpty() and 0 < i < len(self.heap) and 0 < j < len(self.heap):
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def push(self, values):
        self.heap.append(values)
        idx = len(self.heap) - 1
        while 1 < idx:
            pIdx = idx // 2
            if self.heap[pIdx][2] < self.heap[idx][2]:
                break
            self.swap(pIdx, idx)
            idx = pIdx

    def pop(self):
        if self.isEmpty():
            return None
        if 1 == self.size():
            return self.heap.pop()
        ret = self.heap[1]
        print(self.heap[1])
        self.heap[1] = self.heap.pop()
        print(self.heap[1])
        idx = 1
        while idx < len(self.heap):
            tIdx, lIdx, rIdx = idx, 2 * idx, 2 * idx + 1
            if lIdx < len(self.heap) and self.heap[tIdx][2] > self.heap[lIdx][2]:
                tIdx = lIdx
            if rIdx < len(self.heap) and self.heap[tIdx][2] > self.heap[rIdx][2]:
                tIdx = rIdx
            if idx == tIdx:
                break
            self.swap(idx, tIdx)
            idx = tIdx
        return ret


class Solution:
    def kSmallestPairs0(self, nums1, nums2, k):
        if len(nums1) is None or 0 == len(nums1) and len(nums2) is None or 0 == len(nums2):
            return []
        if len(nums1) is None or 0 == len(nums1):
            return nums2[:k]
        if len(nums2) is None or 0 == len(nums2):
            return nums1[:k]

        return [[a, b] for a, b in sorted(product(nums1, nums2), key=lambda t: t[0] + t[1])][:k]

    def kSmallestPairs(self, nums1, nums2, k):
        if len(nums1) is None or 0 == len(nums1) and len(nums2) is None or 0 == len(nums2):
            return []
        if len(nums1) is None or 0 == len(nums1):
            return nums2[:k]
        if len(nums2) is None or 0 == len(nums2):
            return nums1[:k]

        heap, res = MinHeap(), []
        heap.push((0, 0, nums1[0] + nums2[0]))
        while len(res) < k:
            r, c, _ = heap.pop()
            res.append([nums1[r], nums2[c]])
            if r < len(nums1) - 1 and c < len(nums2) - 1:
                heap.push((r + 1, c, nums1[r + 1] + nums2[c]))
                heap.push((r, c + 1, nums1[r] + nums2[c + 1]))
            elif r == len(nums1) - 1 and c < len(nums2) - 1:
                heap.push((r, c + 1, nums1[r] + nums2[c + 1]))
            elif r < len(nums1) - 1 and c == len(nums2) - 1:
                heap.push((r + 1, c, nums1[r + 1] + nums2[c]))
            else:
                break
        return res


s = Solution()
data = [([1,7,11], [2,4,6], 3, [[1,2],[1,4],[1,6]]),
        ([1,1,2], [1,2,3], 2, [[1,1],[1,1]]),
        ([1,2], [3], 3, [[1,3],[2,3]]),
        ]
for nums1, nums2, k, expected in data:
    real = s.kSmallestPairs(nums1, nums2, k)
    print('{}, {}, {}, expected {}, real {}, result {}'.format(nums1, nums2, k, expected, real, expected == real))
