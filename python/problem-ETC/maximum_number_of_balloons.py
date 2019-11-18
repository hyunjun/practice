#   https://leetcode.com/problems/maximum-number-of-balloons


from collections import Counter


class Solution(object):
    #   runtime; 40ms, 18.96%
    #   memory; 12MB, 100.00%
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        cnt, c = float('inf'), Counter(text)
        for ch in 'ban':
            cnt = min(cnt, c[ch])
        if 0 == cnt:
            return 0
        for ch in 'lo':
            cnt = min(cnt, c[ch] // 2)
        return cnt


s = Solution()
data = [('nlaebolko', 1),
        ('loonbalxballpoon', 2),
        ('leetcode', 0),
        ('nlaeolko', 0),
        ('nlaeblko', 0),
        ('loonbalxballpon', 1),
        ]
for text, expected in data:
    real = s.maxNumberOfBalloons(text)
    print(f'{text}, expected {expected}, real {real}, result {expected == real}')
