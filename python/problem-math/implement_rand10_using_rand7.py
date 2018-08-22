#   https://leetcode.com/problems/implement-rand10-using-rand7

#   https://leetcode.com/problems/implement-rand10-using-rand7/solution


class Solution:
    #   48.90%
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            r = (rand7() - 1) * 7 + rand7()
            if 40 < r:
                continue
            res = r % 10
            if 0 == res:
                return 10
            return res
        return -1
