#   https://leetcode.com/problems/check-if-it-is-a-straight-line

#   https://leetcode.com/problems/check-if-it-is-a-straight-line/discuss/432076/Python-simple-solution-100-100


class Solution(object):
    #   runtime; 52ms, 19.83%
    #   memory; 12.1MB, 100.00%
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if 2 == len(coordinates):
            return True

        def getGradient(i):
            if coordinates[i][0] == coordinates[i - 1][0]:
                return float('inf')
            return (coordinates[i][1] - coordinates[i - 1][1]) / (coordinates[i][0] - coordinates[i - 1][0])

        xs, ys = set([x for x, _ in coordinates]), set([y for _, y in coordinates])
        if len(xs) == 1 or len(ys) == 1:
            return True
        gradient = getGradient(1)
        for i in range(2, len(coordinates)):
            curGradient = getGradient(i)
            if curGradient != gradient:
                return False
        return True


s = Solution()
data = [([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]], True),
        ([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]], False),
        ]
for coordinates, expected in data:
    real = s.checkStraightLine(coordinates)
    print(f'{coordinates}, expected {expected}, real {real}, result {expected == real}')
