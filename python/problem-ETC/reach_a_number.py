#   https://leetcode.com/problems/reach-a-number


class Solution:
    #   Time Limit Exceeded
    def reachNumber0(self, target):

        '''
        self.ret, self.visited = float('inf'), set()
        def foo(i, step, cnt):
            if i in self.visited:
                return
            cnt += 1
            if self.ret < cnt:
                return
            if i + step == target or i - step == target:
                self.ret = cnt
                return
            self.visited.add(i)
            foo(i - step, step + 1, cnt)
            foo(i + step, step + 1, cnt)

        foo(0, 1, 0)
        return self.ret
        '''
        q = [(0, 1, 0)]
        while q:
            i, step, cnt = q.pop(0)
            if i == target:
                return cnt
            q.append((i - step, step + 1, cnt + 1))
            q.append((i + step, step + 1, cnt + 1))
        return None

    #   runtime; 156ms, 13.55%
    #   memory; 13.1MB, 7.14%
    def reachNumber(self, target):
        '''
                     0
1/2               -1   1
2/4            -3 -1   1  3
3/7           -6 -4 -2 0 2 4 6
4/10      -10 -8 -6 -4 -2 0 2 4 6 8 10
5/16 -15 -13 -11 -9 -7 -5 -3 -1 1 3 5 7 9 11 13 15
starting point = 0 -1 -3 -6 -10 -15 ... [n] = [n - 1] - step
ending point = 0 1 3 6 10 15 ...
step = 2
        '''
        start, end, cnt = 0, 0, 1
        while True:
            start -= cnt
            end += cnt
            cnt += 1
            #print(start, end)
            if start <= target <= end and target % 2 == end % 2:
                return cnt - 1
            #for i in range(start, end + 1, 2):
            #    if i == target:
            #        return cnt - 1
        return None


s = Solution()
data = [(3, 2),
        (2, 3),
        (-1000000000, 44723),
        ]
for target, expected in data:
    real = s.reachNumber(target)
    print('{}, expected {}, real {}, result {}'.format(target, expected, real, expected == real))
