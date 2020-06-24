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
    def numTrees2(self, n):
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

    #   https://leetcode.com/explore/featured/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3370
    #   runtime; 24ms, 92.98%
    #   memory; 13.7MB, 88.61%
    def numTrees3(self, n: int) -> int:
        if n <= 0:
            return 0
        
        d = {i: 0 for i in range(n + 1)}
        d[0] = d[1] = 1
        def numTree(arr):
            num = len(arr)
            if d[num] != 0:
                return d[num]
            res = sum(numTree(arr[:i]) * numTree(arr[i + 1:]) for i, a in enumerate(arr))
            d[num] = res
            return res
        
        return numTree([i for i in range(1, n + 1)])

    #   https://leetcode.com/explore/featured/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3370
    #   runtime; 28ms, 76.14%
    #   memory; 13.9MB, 27.04%
    def numTrees(self, n: int) -> int:
        if n <= 0:
            return 0
        
        d = {i: 0 for i in range(n + 1)}
        d[0] = d[1] = 1
        def numTree(m):
            if d[m] != 0:
                return d[m]
            res = sum(numTree(i) * numTree(m - (i + 1)) for i in range(m))
            d[m] = res
            return res
        
        return numTree(n)


s = Solution()
data = [(3, 5),
        (5, 42),
        (6, 132),
        ]
for n, expected in data:
    real = s.numTrees(n)
    print('{}, expected {}, real {}, result {}'.format(n, expected, real, expected == real))
