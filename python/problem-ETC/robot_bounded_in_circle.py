#   https://leetcode.com/problems/robot-bounded-in-circle


from typing import List


class Solution:
    #   https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3463
    #   runtime; 40ms, 26.38%
    #   memory; 13.8MB, 71.38%
    def isRobotBounded(self, instructions: str) -> bool:
        if instructions.count('L') == 0 and  instructions.count('R') == 0:
            return False
        if instructions.count('G') == 0:
            return True

        '''
                [0, 1]
        [-1, 0]         [1, 0]
                [0, -1]
        '''
        dirDict = {'N': [0, 1], 'E': [1, 0], 'S': [0, -1], 'W': [-1, 0]}
        def getDirection(direction, instruction):
            if instruction == 'L':
                if direction == dirDict['N']:
                    return dirDict['W']
                if direction == dirDict['W']:
                    return dirDict['S']
                if direction == dirDict['S']:
                    return dirDict['E']
                return dirDict['N']
            elif instruction == 'R':
                if direction == dirDict['N']:
                    return dirDict['E']
                if direction == dirDict['E']:
                    return dirDict['S']
                if direction == dirDict['S']:
                    return dirDict['W']
                return dirDict['N']

        i, direction, point, visited = 0, [0, 1], [0, 0], set()
        for instruction in (instructions * 4):
            if instruction == 'G':
                point[0] += direction[0]
                point[1] += direction[1]
            else:
                direction = getDirection(direction, instruction)
            i += 1
            if i == len(instructions):
                i = 0
        return point[0] == 0 and point[1] == 0


s = Solution()
data = [("GGLLGG", True),
        ("GG", False),
        ("GL", True),
        ("RRRLLRGRLLRLGLLLGRGGGRLLRRGRRLGGRLRRRRLRRLLRR", True),
        ("LRRRRLLLRL", True),
        ("GLGLGGLGL", False),
        ]
for instructions, expect in data:
    real = s.isRobotBounded(instructions)
    print(f'{instructions} expect {expect} real {real} result {expect == real}')
