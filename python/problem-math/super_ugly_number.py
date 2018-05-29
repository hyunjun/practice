#   https://leetcode.com/problems/super-ugly-number


from copy import copy
import heapq


class Solution:

    #   Time Limit Exceeded
    def nthSuperUglyNumber0(self, n, primes):
        if 1 == n:
            return 1
        uglyNumber, queues = 1, []
        for prime in primes:
            queues.append([prime])
        for i in range(2, n + 1):
            uglyNumber = queues[0][0]
            for q in queues:
                if q[0] < uglyNumber:
                    uglyNumber = q[0]
            print('[{}], {}, {}'.format(i, uglyNumber, queues))
            for q in queues:
                if q[0] == uglyNumber:
                    del q[0]
            for i, q in enumerate(queues):
                q.append(uglyNumber * primes[i])
        return uglyNumber

    #   Time Limit Exceeded
    def nthSuperUglyNumber1(self, n, primes):
        if 1 == n:
            return 1
        uglies = copy(primes)
        for i in range(2, n + 1):
            uglyNumber = uglies[0]
            while uglyNumber == uglies[0]:
                del uglies[0]
            for p in primes:
                uglies.append(uglyNumber * p)
            uglies.sort()
        return uglyNumber

    def heapifyDown(self, heap):
        idx, heapLen = 1, len(heap)
        while idx < heapLen:
            lIdx, rIdx = 2 * idx, 2 * idx + 1
            if rIdx < heapLen:
                pVal, lVal, rVal = heap[idx], heap[lIdx], heap[rIdx]
                minVal = min(pVal, lVal, rVal)
                if minVal == pVal:
                    break
                elif minVal == lVal:
                    heap[lIdx], heap[idx] = heap[idx], heap[lIdx]
                    idx = lIdx
                else:
                    heap[rIdx], heap[idx] = heap[idx], heap[rIdx]
                    idx = rIdx
            elif lIdx < heapLen:
                if heap[lIdx] < heap[idx]:
                    heap[lIdx], heap[idx] = heap[idx], heap[lIdx]
                    idx = lIdx
                else:
                    break
            else:
                break

    def heapifyUp(self, heap):
        idx = len(heap) - 1
        while 1 < idx:
            pIdx = idx // 2
            if heap[pIdx] > heap[idx]:
                heap[pIdx], heap[idx] = heap[idx], heap[pIdx]
                idx = pIdx
            else:
                break

    #   Time Limit Exceeded
    def nthSuperUglyNumber1(self, n, primes):
        if 1 == n:
            return 1
        heap = copy(primes)
        heap.insert(0, None)
        for i in range(2, n + 1):
            uglyNumber = heap[1]
            while uglyNumber == heap[1]:
                heap[1] = heap.pop()
                self.heapifyDown(heap)
            for p in primes:
                heap.append(uglyNumber * p)
                self.heapifyUp(heap)
        return uglyNumber

    #   Time Limit Exceeded
    def nthSuperUglyNumber2(self, n, primes):
        if 1 == n:
            return 1
        heap, s = copy(primes), set()
        heap.insert(0, None)
        for i in range(2, n + 1):
            uglyNumber = heap[1]
            heap[1] = heap.pop()
            self.heapifyDown(heap)
            for p in primes:
                cand = uglyNumber * p
                if cand in s:
                    continue
                else:
                    s.add(cand)
                    heap.append(cand)
                    self.heapifyUp(heap)
        return uglyNumber

    #   Time Limit Exceede for the last test case
    def nthSuperUglyNumber3(self, n, primes):
        if 1 == n:
            return 1
        heap, s, maxVal = copy(primes), set(), 2 ** 32 - 1
        heap.insert(0, None)
        for i in range(2, n + 1):
            uglyNumber = heap[1]
            if 2 < len(heap):
                heap[1] = heap.pop()
                self.heapifyDown(heap)
            else:
                heap.pop()
            for p in primes:
                cand = uglyNumber * p
                if maxVal < cand or cand in s:
                    continue
                else:
                    s.add(cand)
                    heap.append(cand)
                    self.heapifyUp(heap)
            #print(heap)
        return uglyNumber

    #   https://leetcode.com/problems/super-ugly-number/discuss/130206/easy-understand-python-solution-using-heap
    #   9.82%
    def nthSuperUglyNumber(self, n, primes):
        uglyNumber = 0
        heap = [1]
        s, maxVal = set(), 2 ** 32 - 1
        while 0 < n:
            uglyNumber = heapq.heappop(heap)
            n -= 1
            for prime in primes:
                cand = uglyNumber * prime
                if maxVal < cand or cand in s:
                    continue
                else:
                    s.add(cand)
                    heapq.heappush(heap, cand)
        return uglyNumber


s = Solution()
data = [(2, [2], 2),
        (3, [2], 4),
        (12, [2, 7, 13, 19], 32),
        (10, [5,11,17,23,31,43,47,53,59,67,73,83,97,107,109,131,139,149,163,181,191,193,197,199,211,223,227,229,241,263], 53),
        (20, [2,3,7,11,13,17,29,31,53,73,79,83,89,97,109,113,127,131,139,149,151,173,179,191,193,197,199,227,239,241], 27),
        (100000, [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251], 1092889481),
        (4000, [2,3,5,13,19,29,31,41,43,53,59,73,83,89,97,103,107,109,127,137,139,149,163,173,179,193,197,199,211,223,227,229,239,241,251,257,263,269,271,281,317,331,337,347,353,359,367,373,379,389,397,409,419,421,433,449,457,461,463,479,487,509,521,523,541,547,563,569,577,593,599,601,613,619,631,641,659,673,683,701,709,719,733,739,743,757,761,769,773,809,811,829,857,859,881,919,947,953,967,971], 15132),
        ]
for n, primes, expected in data:
    real = s.nthSuperUglyNumber(n, primes)
    print('{}, {}, expected {}, real {}, result {}'.format(n, primes, expected, real, expected == real))
