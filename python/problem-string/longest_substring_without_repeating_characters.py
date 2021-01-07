#   https://leetcode.com/problems/longest-substring-without-repeating-characters

#   https://leetcode.com/problems/longest-substring-without-repeating-characters/solution


from collections import defaultdict


class Solution:
    #   https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3595
    #   runtime; 64ms, 63.44%
    #   memory; 14.3MB, 48.64%
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or 0 == len(s):
            return 0
        sIdx, maxLen, d = 0, 0, defaultdict(int)
        for i, c in enumerate(s):
            if c in d:
                nIdx = d[c] + 1
                for j in range(sIdx, nIdx):
                    del d[s[j]]
                sIdx = nIdx
            d[c] = i
            maxLen = max(maxLen, i - sIdx + 1)
        return maxLen


solution = Solution()
data = [('abcabcbb', 3),
        ('bbbbb', 1),
        ('pwwkew', 3),
        ('', 0),
        ]
for s, expect in data:
    real = solution.lengthOfLongestSubstring(s)
    print(f'{s} expect {expect} real {real} result {expect == real}')
