#   https://leetcode.com/problems/minimum-absolute-difference


class Solution(object):
    #   runtime; 316ms, 95.29%
    #   memory; 22.6MB, 100.00%
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        minDiff, res, sortedArr = float('inf'), [], sorted(arr)
        for i in range(1, len(arr)):
            curDiff = sortedArr[i] - sortedArr[i - 1]
            if minDiff < curDiff:
                continue
            elif minDiff == curDiff:
                res.append([sortedArr[i - 1], sortedArr[i]])
            else:
                minDiff, res = curDiff, [[sortedArr[i - 1], sortedArr[i]]]
        return res


s = Solution()
data = [([4,2,1,3], [[1,2],[2,3],[3,4]]),
        ([1,3,6,10,15], [[1,3]]),
        ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
        ]
for arr, expected in data:
    real = s.minimumAbsDifference(arr)
    print(f'{arr}, expected {expected}, real {real}, result {expected == real}')
