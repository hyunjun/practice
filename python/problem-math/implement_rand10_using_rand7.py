#   https://leetcode.com/problems/implement-rand10-using-rand7

#   https://leetcode.com/problems/implement-rand10-using-rand7/solution


class Solution:
    #   48.90%
    def rand10_0(self):
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

    #   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3439
    #   runtime; 332ms, 91.94%
    #   memory; 16.5MB, 75.41%
    def rand10(self):
        """
        :rtype: int
        """
        r = (rand7() - 1) * 7 + rand7()
        if 1 <= r <= 40:
            res = r % 10
            return 10 if res == 0 else res
        return self.rand10()
