#   https://leetcode.com/problems/pascals-triangle
#   34.84%

#   https://leetcode.com/problems/pascals-triangle/solution


class Solution:
    def generate(self, numRows):
        if numRows <= 0:
            return []
        if 1 == numRows:
            return [[1]]
        result = [[1], [1, 1]]
        for numRow in range(2, numRows):
            prevNums = result[numRow - 1]
            nums = [prevNums[i] + prevNums[i + 1] for i in range(numRow - 1)]
            nums.insert(0, 1)
            nums.append(1)
            result.append(nums)
        return result


s = Solution()
print(s.generate(5))
