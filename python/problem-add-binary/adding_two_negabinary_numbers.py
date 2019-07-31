#   https://leetcode.com/problems/adding-two-negabinary-numbers

#   https://leetcode.com/problems/adding-two-negabinary-numbers/discuss/344150/Python-simple-solution-add-digit-by-digit-and-carry


from typing import List
import math


class Solution:
    def addNegabinary0(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if arr1 == [0]:
            return arr2
        if arr2 == [0]:
            return arr1

        def arr2num(arr):
            '''
            _sum = 0
            for i, a in enumerate(arr):
                if 0 == a:
                    continue
                _sum += math.pow(-2, len(arr) - i - 1)
            return _sum
            '''
            return sum(math.pow(-2, len(arr) - i - 1) if 1 == a else 0 for i, a in enumerate(arr))

        num = arr2num(arr1) + arr2num(arr2)
        #print(f'{arr2num(arr1)} + {arr2num(arr2)} = {num}')

        if 0 == num:
            return [0]
        maxNum, numLen, arrLen = 1, 2, 1
        while maxNum < num:
            maxNum += math.pow(2, numLen)
            numLen *= 2
            arrLen += 2
        i, arr = 0, [0] * arrLen
        arr[0] = 1
        num -= math.pow(-2, arrLen - 1)
        for i in range(1, arrLen):
            bitNum = math.pow(-2, len(arr) - i - 1)
            if i % 2 == 0:
                #print(f'{i}, {bitNum}, {num}')
                if bitNum <= num:
                    arr[i] = 1
                    num -= bitNum
            else:
                bitNum2 = math.pow(-2, len(arr) - i - 3)
                #print(f'{i}, {bitNum}, {bitNum2}, {num}')
                if bitNum <= num < bitNum2:
                    arr[i] = 1
                    num -= bitNum
            #print(f'{arr}, {num}')
        return arr

    #   runtime; 76ms, 59.26%
    #   memory; 13.9MB, 100.00%
    def addNegabinary1(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if arr1 == [0]:
            return arr2
        if arr2 == [0]:
            return arr1
        l1, l2 = len(arr1), len(arr2)
        if l1 < l2:
            l, s = arr2, arr1
        else:
            l, s = arr1, arr2
        ll, ls = len(l), len(s)
        a1, a2, sArr = [0] * (ll + 2), [0] * (ll + 2), [0] * (ll + 2)
        #print(f'{l}, {s}, {a1}, {a2}, {sArr}')
        j = 0
        for i in range(ll - 1, -1, -1):
            a1[j] = l[i]
            j += 1
        j = 0
        for i in range(ls - 1, -1, -1):
            a2[j] = s[i]
            j += 1
        #print(f'{l}, {s}, {a1}, {a2}, {sArr}')
        for i in range(ll + 2):
            ones = sorted([a1[i], a2[i], sArr[i]])
            if ones == [0, 0, 0]:
                continue
            if ones == [0, 0, 1]:
                sArr[i] = 1
                continue
            if ones == [0, 1, 1]:
                sArr[i] = 0
            elif ones == [1, 1, 1]:
                sArr[i] = 1
            if sArr[i + 1] == 1:
                sArr[i + 1] = 0
            else:
                sArr[i + 1] = 1
                sArr[i + 2] += 1
        i = ll + 1
        while 1 < len(sArr) and sArr[i] == 0:
            sArr.pop()
            i -= 1
        #print(f'{l}, {s}, {a1}, {a2}, {sArr}')
        return sArr[::-1]

    #   runtime; 68ms, 86.67%
    #   memory; 13.9MB, 100.00%
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if arr1 == [0]:
            return arr2
        if arr2 == [0]:
            return arr1
        l1, l2 = len(arr1), len(arr2)
        if l1 < l2:
            l, s = arr2, arr1
        else:
            l, s = arr1, arr2
        ll, ls = len(l), len(s)
        a1, a2, sArr = [0] * (ll + 2), [0] * (ll + 2), [0] * (ll + 2)
        j = 0
        for i in range(ll - 1, -1, -1):
            a1[j] = l[i]
            j += 1
        j = 0
        for i in range(ls - 1, -1, -1):
            a2[j] = s[i]
            j += 1
        for i in range(ll + 2):
            _sum = sum([a1[i], a2[i], sArr[i]])
            if _sum == 0:
                continue
            if _sum == 1:
                sArr[i] = 1
                continue
            if _sum == 2:
                sArr[i] = 0
            elif _sum == 3:
                sArr[i] = 1
            if sArr[i + 1] == 1:
                sArr[i + 1] = 0
            else:
                sArr[i + 1] = 1
                sArr[i + 2] += 1
        i = ll + 1
        while 1 < len(sArr) and sArr[i] == 0:
            sArr.pop()
            i -= 1
        return sArr[::-1]

s = Solution()
data = [([1, 1, 1, 1, 1], [1, 0, 1], [1, 0, 0, 0, 0]),
        ([1, 1, 1, 1, 1], [1, 1, 1], [1, 0, 0, 1, 0]),
        ([1, 1, 1, 1, 0], [1, 0, 1], [1, 0, 0, 1, 1]),
        ([1, 1, 0, 0, 1], [1, 0, 0], [1, 1, 1, 0, 1]),
        ([1, 1, 1, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1]),
        ([1], [1], [1, 1, 0]),
        ([1], [1, 1], [0]),
        ]
for arr1, arr2, expected in data:
    real = s.addNegabinary(arr1, arr2)
    print(f'{arr1}, {arr2}, expected {expected}, real {real}, result {expected == real}')
