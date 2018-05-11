#   https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
#   33.57%


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        idxDict = {}
        for i, n in enumerate(numbers):
            m = target - n
            if m in idxDict:
                return [idxDict[m] + 1, i + 1]
            idxDict[n] = i
        return [None, None]

s = Solution()
data = [([2, 7, 11, 15], 9, [1, 2]),
        ([3, 3], 6, [1, 2]),
        ([3, 2, 4], 6, [2, 3]),
        ([-3, 4, 3, 90], 0, [1, 3])
        ]
for numbers, target, expected in data:
    real = s.twoSum(numbers, target)
    print(f'{numbers}, target {target}, expected {expected}, real {real}, result {expected == real}')
