#   https://leetcode.com/problems/reverse-words-in-a-string


import re


class Solution:
    #   97.88%
    def reverseWords0(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        l, r = 0, len(words) - 1
        while l < r:
            words[l], words[r] = words[r].strip(), words[l].strip()
            l += 1
            r -= 1
        return ' '.join(words)

    #   https://www.youtube.com/watch?v=aotBpjJUqJo
    #   runtime; 64ms, 6.77%
    #   memory; 13.8MB, 5.16%
    def reverseWords1(self, s):
        l = []
        for i, c in enumerate(s.strip()):
            if c == ' ' and l[-1] == ' ':
                continue
            l.append(c)

        def reverse(i, j):
            while i < j:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1

        reverse(0, len(l) - 1)
        s = 0
        for i, c in enumerate(l):
            if c == ' ':
                reverse(s, i - 1)
                s = i + 1
        reverse(s, len(l) - 1)
        return ''.join(l)

    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3391
    #   runtime; 48ms, 25.05%
    #   memory; 14.2MB, 95.62%
    def reverseWords2(self, s: str) -> str:
        return ' '.join(re.sub('\s+', ' ', s.strip()).split(' ')[::-1])

    #   runtime; 28ms, 83.77%
    #   memory; 14.6MB, 12.96%
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])


s = Solution()
data = [("the sky is blue", "blue is sky the"),
        ('perfect makes practice', 'practice makes perfect'),
        ('a good  example', 'example good a'),
        ]
for inp, expected in data:
    real = s.reverseWords(inp)
    print(f'{inp}, expected {expected}, real {real}, result {expected == real}')
