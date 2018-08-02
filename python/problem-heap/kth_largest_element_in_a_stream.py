#   https://leetcode.com/problems/kth-largest-element-in-a-stream


#   14.17%
class KthLargest:
    def __init__(self, k, nums):
        self.h = [None]
        self.k = k
        self.heapify(nums)
        print(self.h)

    def heapify(self, nums):
        ret = None
        print('before', nums, self.h)
        for n in nums:
            if len(self.h) < self.k + 1 or self.h[1] <= n:
                self.h.append(n)
                i = len(self.h) - 1
                while 1 < i:
                    pIdx = i // 2
                    if self.h[pIdx] > self.h[i]:
                        self.h[pIdx], self.h[i] = self.h[i], self.h[pIdx]
                    i = pIdx
                if self.k + 1 < len(self.h):
                    ret = self.heappop()
        print('after', nums, self.h)
        return ret

    def add(self, val):
        self.heapify([val])
        return self.h[1]

    def heappop(self):
        if len(self.h) < 2:
            return None
        if len(self.h) == 2:
            return self.h.pop()
        ret = self.h[1]
        self.h[1] = self.h.pop()
        i = 1
        while i < len(self.h):
            lIdx, rIdx = 2 * i, 2 * i + 1
            swapIdx = lIdx
            if rIdx < len(self.h):
                if self.h[lIdx] > self.h[rIdx]:
                    swapIdx = rIdx
            if swapIdx < len(self.h):
                if self.h[i] > self.h[swapIdx]:
                    self.h[i], self.h[swapIdx] = self.h[swapIdx], self.h[i]
            i = swapIdx
        return ret


import heapq


#   https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/148866/Python-simple-heapq-solution-beats-100
class KthLargest1:

    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        self.size = len(self.pool)
        heapq.heapify(self.pool)
        while self.size > k:
            heapq.heappop(self.pool)
            self.size -= 1

    def add(self, val):
        print(val, self.pool)
        if self.size < self.k:
            heapq.heappush(self.pool, val)
            self.size += 1
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        print('after', self.pool)
        return self.pool[0]


k = KthLargest(3, [4, 5, 8, 2])
print(k.add(3))
print(k.add(5))
print(k.add(10))
print(k.add(9))
print(k.add(4))
