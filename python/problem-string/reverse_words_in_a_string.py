#   https://leetcode.com/problems/reverse-words-in-a-string


class Solution(object):
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
    def reverseWords(self, s):
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
        
s = Solution()
data = [("the sky is blue", "blue is sky the"),
        ('perfect makes practice', 'practice makes perfect'),
        ('a good  example', 'example good a'),
        ]
for inp, expected in data:
    real = s.reverseWords(inp)
    print(f'{inp}, expected {expected}, real {real}, result {expected == real}')
