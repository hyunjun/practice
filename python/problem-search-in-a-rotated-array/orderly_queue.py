#   https://leetcode.com/problems/orderly-queue

#   https://leetcode.com/problems/orderly-queue/solution
#   https://hackernoon.com/fun-with-array-rotations-add4a335d79a


class Solution:
    #   RuntimeError: maximum recursion depth exceeded in cmp
    def orderlyQueue0(self, S, K):
        if S is None or 0 == len(S) or K < 1:
            return S
        self.ans, self.ansSet = S, set()
        def getOrdered(w):
            print(w)
            isOrdered, self.ans = True, min(self.ans, w)
            if w in self.ansSet:
                print('same')
                return
            self.ansSet.add(w)
            for i, c in enumerate(w):
                if 0 == i:
                    continue
                if w[i - 1] > c:
                    isOrdered = False
                    break
            if isOrdered:
                self.ans = w
                return
            for i, c in enumerate(w):
                if K <= i:
                    break
                getOrdered(w[:i] + w[i + 1:] + c)
        for i, c in enumerate(S):
            if K <= i:
                break
            cand = S[:i] + S[i + 1:] + c
            if cand in self.ansSet:
                continue
            getOrdered(cand)
        return self.ans

    #   runtime; 16ms, 100.00%
    #   memory; 10.7MB, 66.67%
    def orderlyQueue(self, S, K):
        if S is None or 0 == len(S) or K < 1:
            return S
        if 1 == K:
            minChar, minStr = min(S), S
            for i in range(len(S) - 1, -1, -1):
                if S[i] == minChar:
                    minStr = min(minStr, minChar + S[i + 1:] + S[:i])
            return minStr
        return ''.join(sorted(S))


s = Solution()
data = [('cba', 1, 'acb'),
        ('baaca', 3, 'aaabc'),
        ('xyokshvwx', 9, 'hkosvwxxy'),
        ('nhtq', 1, 'htqn'),
        ('enbczfjtvxerzbrvigpl', 1, 'bczfjtvxerzbrvigplen'),
        ]
for S, K, expected in data:
    real = s.orderlyQueue(S, K)
    print('{}, {}, expected {}, real {}, result {}'.format(S, K, expected, real, expected == real))
