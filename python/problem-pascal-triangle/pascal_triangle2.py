#   https://leetcode.com/problems/pascals-triangle-ii


class Solution:

    #   98.22%
    def getRow(self, rowIndex):
        if rowIndex < 0:
            return []
        if 0 == rowIndex:
            return [1]
        result = [1, 1]
        for numRow in range(2, rowIndex + 1):
            nums = [result[i] + result[i + 1] for i in range(numRow - 1)]
            nums.insert(0, 1)
            nums.append(1)
            result = nums
        return result

    #   https://leetcode.com/problems/pascals-triangle-ii/discuss/38467/Very-simple-Python-solution
    def getRow1(self, rowIndex):
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row


s = Solution()
for i in range(5):
    print(s.getRow(i))
for i in range(5):
    print(s.getRow1(i))
