#   https://leetcode.com/problems/max-consecutive-ones-iii


class Solution:
    #   runtime; 156ms, 47.51%
    #   memory; 11.5MB, 100.00%
    def longestOnes(self, A, K):
        if A is None or 0 == len(A):
            return 0
        if 0 == K:
            start, cnt = -1, 0
            for i, a in enumerate(A):
                if (0 == i or 0 == A[i - 1]) and 1 == a:
                    start = i
                if (0 < i and 1 == A[i - 1] and 0 == a):
                    cnt = max(cnt, i - start)
                elif len(A) - 1 == i and 1 == a:
                    cnt = max(cnt, i - start + 1)
            return cnt

        zeroIndices, cnt = [i for i, a in enumerate(A) if 0 == a], 0
        if len(zeroIndices) <= K:
            return len(A)
        #print(zeroIndices)
        for i, zeroIndex in enumerate(zeroIndices):
            if len(zeroIndices) - K < i:
                break
            firstReplaced, lastReplaced = i, i + K - 1
            #if 0 < firstReplaced:
            #    print('zeroIndex[{}] + 1 == {} {}\t0 -> 1 {}~{}'.format(firstReplaced - 1, zeroIndex, zeroIndices[firstReplaced - 1] + 1 == zeroIndex, firstReplaced, lastReplaced))
            #else:
            #    print('0 -> 1 {}~{}'.format(firstReplaced, lastReplaced))
            if 0 == zeroIndex or 0 < firstReplaced and zeroIndices[firstReplaced - 1] + 1 == zeroIndex:
                startIndex = zeroIndex
            else:
                if 0 == firstReplaced:
                    startIndex = 0
                else:
                    startIndex = zeroIndices[firstReplaced - 1] + 1
            if len(A) - 1 == zeroIndex or lastReplaced < len(zeroIndices) - 1 and zeroIndex + 1 == zeroIndices[lastReplaced + 1]:
                lastIndex = zeroIndex
            else:
                if len(zeroIndices) - 1 == lastReplaced:
                    lastIndex = len(A) - 1
                else:
                    lastIndex = zeroIndices[lastReplaced + 1] - 1
            cnt = max(cnt, lastIndex - startIndex + 1)
            #print('0 -> 1 {}~{} start {} last {} cnt {}'.format(firstReplaced, lastReplaced, startIndex, lastIndex, cnt))
        return cnt


s = Solution()
data = [([1,1,1,0,0,0,1,1,1,1,0], 0, 4),
        ([1], 0, 1),
        ([0, 1], 0, 1),
        ([1,1,1,0,0,0,1,1,1,1,0], 2, 6),
        ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10),
        ([0, 0, 0, 1], 4, 4),
        ([1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1], 8, 25),
        ]
for A, K, expected in data:
    real = s.longestOnes(A, K)
    print('{}, {}, expected {}, real {}, result {}'.format(A, K, expected, real, expected == real))
'''
1 1 1 0 0 0 1 1 1 1 0
    2 3 4 5 6       10 11
1 1 1 1 1
        1 1 1 1 1 1
          1 1 1 1 1 1
               0  1  2  3
zeroIndices = [3, 4, 5, 10]
f, l = 0, 1 -> s = 0, l = 4 -> cnt = 4 - 0 + 1 = 5
f, l = 1, 2 -> s = 4, l = 9 -> cnt = 9 - 4 + 1 = 6
f, l = 2, 3 -> s = 5, l = 10 -> cnt = 10 - 5 + 1 = 6

0 0 1 1 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1
0 1     4 5       9    121314
1 1 1 1 1
  1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
          1 1 1 1 1 1 1 1
            1 1 1 1 1 1 1 1
                    1 1 1 1 1 1 1 1 1
#   zList = get indices of value 0s
#   replace K zeroes in zList, then calculate the length
#       1. first replaced zero
#           index = 0 or there is another 0 value index in left -> start index
#           there is a 1 value index in left -> start index = anthoer 0 value index in left + 1
#       2. last replaced zero
#           index = len(A) - 1 or there is another 0 value index in right -> end index 
#           there is a 1 value index in right -> end index = another 0 value index in right - 1
'''
