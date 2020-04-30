#   https://leetcode.com/explore/featured/card/recursion-i/250/principle-of-recursion/1440


from typing import List


class Solution:
    #   runtime; 216ms, 52.42%
    #   memory; 18.4MB
    def reverseString(self, s: List[str]) -> None:
        if s is None or 0 == len(s):
            return
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
