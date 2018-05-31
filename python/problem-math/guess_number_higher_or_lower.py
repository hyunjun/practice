#   https://leetcode.com/problems/guess-number-higher-or-lower
#   23.94%

#   https://leetcode.com/problems/guess-number-higher-or-lower/solution


class Solution(object):
    def guessNumber(self, n):
        l, r, s = 1, n, set()
        while True:
            m = (l + r) // 2
            guessed = guess(m)
            if 0 == guessed:
                return m
            if -1 == guessed:
                if m in s:
                    r = m - 1
                else:
                    s.add(m)
                    r = m
            elif 1 == guessed:
                if m in s:
                    l = m + 1
                else:
                    s.add(m)
                    l = m
        return guessed
