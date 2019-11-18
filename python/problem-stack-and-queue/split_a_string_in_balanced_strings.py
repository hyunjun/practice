#   https://leetcode.com/problems/split-a-string-in-balanced-strings


class Solution(object):
    #   runtime; 20ms, 53.22%
    #   memory; 11.7MB, 100.00%
    def balancedStringSplit0(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt, stack = 0, []
        for c in s:
            if 0 == len(stack) or stack[-1] == c:
                stack.append(c)
            else:
                stack.pop()
            if 0 == len(stack):
                cnt += 1
        return cnt

    #   runtime; 20ms, 53.22%
    #   memory; 11.7MB, 100.00%
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        lc, rc, cnt = 0, 0, 0
        for c in s:
            if c == 'L':
                lc += 1
            elif c == 'R':
                rc += 1
            if lc == rc:
                cnt += 1
        return cnt


solution = Solution()
data = [('RLRRLLRLRL', 4),
        ('RLLLLRRRLR', 3),
        ('LLLLRRRR', 1),
        ('RLRRRLLRLL', 2),
        ]
for s, expected in data:
    real = solution.balancedStringSplit(s)
    print(f'{s}, expected {expected}, real {real}, result {expected == real}')
