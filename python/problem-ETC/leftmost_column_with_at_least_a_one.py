#   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3306


class Solution:
    #   runtime; 108ms
    #   memory; 14MB
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        curMax = -1
        for r in range(m - 1, -1, -1):
            if 0 == binaryMatrix.get(r, n - 1):
                continue
            minC, maxC = 0, n - 1
            while minC <= maxC:
                c = (minC + maxC) // 2
                if 1 == binaryMatrix.get(r, c):
                    curMax = c if curMax == -1 else min(curMax, c)
                    maxC = c - 1
                else:
                    minC = c + 1
        return curMax
