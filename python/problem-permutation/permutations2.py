# https://leetcode.com/problems/permutations-ii/description/

from collections import Counter
from typing import List


class Solution:
    def __init__(self):
        self.result = []

    # 29.34%
    # 전체 permutation을 모두 만들고 중복을 제거하면 느림
    # unique한 number를 node value로 갖는 tree를 만들어
    # root부터 leaf까지 value들을 하나의 permutation으로 생각하면 됨
    # 예를 들어 1, 2, 1이라면 다음과 같이 3개의 leaf를 갖는 tree가 됨
    #    root
    #    /  |
    #   1   2
    #  / |  |
    # 1  2  1
    # |  |  |
    # 2  1  1
    def recur(self, countDict, perm):
        #print('recur {} perm {}'.format(countDict, perm))
        vals = set(countDict.values())
        if {0} == vals:
            #print(perm)
            self.result.append(perm[:])
        else:
            for k, v in countDict.copy().items():
                if 0 == v:
                    continue
                #print('k {} v {}'.format(k, v))
                countDict[k] -= 1
                perm.append(k)
                #print('before call; recur {} perm {}'.format(countDict, perm))
                self.recur(countDict, perm)
                countDict[k] += 1
                perm.pop()
                #print(' after call; recur {} perm {}'.format(countDict, perm))

    def permuteUnique0(self, nums):
        if nums is None or 0 == len(nums):
            return []
        if 1 == len(nums):
            return [nums]

        countDict = Counter(nums)
        #print(countDict)
        self.recur(countDict, [])

        return self.result

    #   https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3528
    #   runtime; 328ms, 22.26%
    #   memory; 14.7MB
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        self.res = set()

        def permutation(acc, arr):
            if 0 == len(arr):
                self.res.add(tuple(acc))
            else:
                for i, a in enumerate(arr):
                    acc.append(a)
                    permutation(acc, arr[:i] + arr[i + 1:])
                    acc.pop()

        permutation([], nums)
        return list(list(r) for r in self.res)


s = Solution()
data = [([1, 2, 1], 3),
        ([1, 2, 1, 2], 6),
        ([0, 1, 1, 2, 0, 1, 2, 0], 560),
        ]
for nums, expectLen in data:
    real = s.permuteUnique(nums)
    print(f'{nums} expect len {expectLen} real len {len(real)} result {expectLen == len(real)}')
