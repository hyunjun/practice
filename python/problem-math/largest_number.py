#   https://leetcode.com/problems/largest-number

#   https://leetcode.com/problems/largest-number/solution


from functools import cmp_to_key
from typing import List


class Solution:
    #   Wrong Answer
    def largestNumber0(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        maxLen = max([len(str(n)) for n in nums])
        strNums = []
        for i, n in enumerate(nums):
            strNum = str(n)
            while len(strNum) < maxLen:
                #strNum += strNum[-1]
                strNum += strNum[0]
            strNums.append((i, int(strNum)))
        res = []
        for i, _ in sorted(strNums, key=lambda t: t[1], reverse=True):
            res.append(nums[i])
        while 1 < len(res) and 0 == res[0]:
            res.pop(0)
        return ''.join([str(r) for r in res])

    #   34.98%
    def largestNumber1(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        numListDict = {}
        for n in nums:
            firstDigit = int(str(n)[0])
            if firstDigit in numListDict:
                inputIdx = len(numListDict[firstDigit])
                for i, d in enumerate(numListDict[firstDigit]):
                    if int(str(n) + str(d)) > int(str(d) + str(n)):
                        inputIdx = i
                        break
                numListDict[firstDigit].insert(inputIdx, n)
            else:
                numListDict[firstDigit] = [n]
        res = []
        for _, numList in sorted(numListDict.items(), key=lambda t: t[0], reverse=True):
            res.extend(numList)
        while 1 < len(res) and 0 == res[0]:
            res.pop(0)
        return ''.join([str(r) for r in res])

    #   https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3472
    #   runtime; 36ms, 84.93%
    #   memory; 14.1MB
    def largestNumber2(self, nums: List[int]) -> str:
        maxLen = max(len(str(n)) for n in nums)
        sortedNums = sorted([(n, int(str(n) + str(n)[-1] * (maxLen - len(str(n))))) for n in nums], key=lambda t: -t[1])
        for i, (n, modified) in enumerate(sortedNums):
            if 0 == i:
                continue
            prevNum = sortedNums[i - 1][0]
            if str(prevNum)[0] == str(n)[0] and int(str(prevNum) + str(n)) < int(str(n) + str(prevNum)):
                sortedNums[i - 1], sortedNums[i] = sortedNums[i], sortedNums[i - 1]
        return str(int(''.join(str(n) for n, _ in sortedNums)))

    #   runtime; 44ms, 52.70%
    #   memory; 14.1MB, 5.29%
    def largestNumber(self, nums: List[int]) -> str:

        def comparator(a, b):
            strA, strB = str(a), str(b)
            firstA, firstB = int(strA[0]), int(strB[0])
            if firstA > firstB:
                return -1
            if firstA < firstB:
                return 1
            numAB, numBA = int(strA + strB), int(strB + strA)
            if numAB > numBA:
                return -1
            if numAB < numBA:
                return 1
            return 0

        return str(int(''.join([str(n) for n in sorted(nums, key=cmp_to_key(comparator))])))


s = Solution()
data = [([10, 2], '210'),
        ([3, 30, 34, 5, 9], '9534330'),
        ([0, 0], '0'),
        ([824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247], '9609938824824769735703560743981399'),
        ([121, 12], '12121'),
        ([128, 12], '12812'),
        ([9145, 1077, 9647, 9248, 9007, 3912, 7934, 3908, 3109], '964792489145900779343912390831091077'),
        ]
for nums, expect in data:
    real = s.largestNumber(nums)
    print(f'{nums}\n\texpect\t{expect}\n\treal\t{real}\n\tresult\t{expect == real}')
'''
121 12 -> 12 > 121
128 12 -> 128 > 12
8247 824 -> 824 > 8247
8249 824 -> 8249 > 824
8249 82  -> 82 > 8249
            824982
            828249
8241 82  -> 82 > 8241
            824182
            828241
'''
