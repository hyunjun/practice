#   https://leetcode.com/problems/reverse-words-in-a-string
#   97.88%


class Solution(object):
    def reverseWords(self, s):
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
        
s = Solution()
data = [("the sky is blue", "blue is sky the")]
for inp, expected in data:
    real = s.reverseWords(inp)
    print(f'{inp}, expected {expected}, real {real}, result {expected == real}')
