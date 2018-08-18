#   https://leetcode.com/problems/largest-number

#   https://leetcode.com/problems/largest-number/solution


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
    def largestNumber(self, nums):
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


s = Solution()
data = [([10, 2], '210'),
        ([3, 30, 34, 5, 9], '9534330'),
        ([0, 0], '0'),
        ([824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247], '9609938824824769735703560743981399'),
        ([121, 12], '12121'),
        ([9145, 1077, 9647, 9248, 9007, 3912, 7934, 3908, 3109], '964792489145900779343912390831091077'),
        ]
for nums, expected in data:
    real = s.largestNumber(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
