#   https://leetcode.com/problems/unique-binary-search-trees

#   https://en.wikipedia.org/wiki/Catalan_number
#   결과의 갯수가 catalan number


from TreeNode import TreeNode
from collections import defaultdict

class Solution:
    #   Wrong Answer
    def numTrees0(self, n):
        if n <= 0:
            return 0

        def getNumTrees(nList):
            if 1 == len(nList):
                return 1
            cnt = 0
            print(nList)
            for i, n in enumerate(nList):
                print('\t', nList[:i], nList[i + 1:])
                lList, rList = nList[:i], nList[i + 1:]
                if len(lList) <= 1 and len(rList) <= 1:
                    cnt += 1
                elif len(lList) <= 1:
                    cnt += getNumTrees(rList)
                elif len(rList) <= 1:
                    cnt += getNumTrees(lList)
                else:
                    cnt += getNumTrees(lList) + getNumTrees(rList)
            print(nList, cnt)
            return cnt

        return getNumTrees([n for n in range(1, n + 1)])

    #   Time Limit Exceede
    def numTrees1(self, n):
        if n <= 0:
            return 0

        d = defaultdict(int)

        def getNumTrees(nList):
            key = ','.join([str(n) for n in nList])
            if key in d:
                print('[{}] {}'.format(key, d[key]))
                return d[key]
            if 1 == len(nList):
                return 1
            cnt = 0
            print(nList)
            for i, n in enumerate(nList):
                print('\t', nList[:i], nList[i + 1:])
                lList, rList = nList[:i], nList[i + 1:]
                if len(lList) <= 1 and len(rList) <= 1:
                    cnt += 1
                elif len(lList) <= 1:
                    cnt += getNumTrees(rList)
                elif len(rList) <= 1:
                    cnt += getNumTrees(lList)
                else:
                    cnt += getNumTrees(lList) * getNumTrees(rList)
            d[key] = cnt
            print(nList, cnt)
            return cnt

        return getNumTrees([n for n in range(1, n + 1)])

    #   runtime; 20ms, 90.35%
    #   memory; 10.8MB, 100.00%
    def numTrees(self, n):
        if n <= 0:
            return 0

        d = defaultdict(int)
        d[1] = 1

        def getNumTrees(n):
            if n in d or n <= 1:
                return d[n]
            cnt = 0
            for lNum in range(n):
                rNum = n - 1 - lNum
                if lNum <= 1 and rNum <= 1:
                    cnt += 1
                elif lNum <= 1:
                    cnt += getNumTrees(rNum)
                elif rNum <= 1:
                    cnt += getNumTrees(lNum)
                else:
                    cnt += getNumTrees(lNum) * getNumTrees(rNum)
            d[n] = cnt
            return cnt

        return getNumTrees(n)


s = Solution()
data = [(3, 5),
        (5, 42),
        (6, 132),
        ]
for n, expected in data:
    real = s.numTrees(n)
    print('{}, expected {}, real {}, result {}'.format(n, expected, real, expected == real))
