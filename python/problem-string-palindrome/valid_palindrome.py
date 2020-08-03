# https://leetcode.com/problems/valid-palindrome


import re


class Solution(object):
    #   1.58% of python submissions
    def isPalindrome0(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = []
        for c in s.lower():
            if c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                cleaned.append(c)
        ss = ''.join(cleaned)
        return ss == ss[::-1]

    #   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3411
    #   runtime; 36ms, 97.14%
    #   memory; 15.4MB, 14.20%
    def isPalindrome(self, s: str) -> bool:
        r = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return r == r[::-1]


s = Solution()
data = [('', True),
        ('A man, a plan, a canal: Panama', True),
        ('race a car', False),
        ]
for cand, expect in data:
    real = s.isPalindrome(cand)
    print(f'{cand} expect {expect} real {real} result {expect == real}')
