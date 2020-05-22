#   https://leetcode.com/problems/sort-characters-by-frequency


from collections import Counter

class Solution:
    #   runtime; 56ms, 62.66%
    #   memory; 12.6MB, 86.03%
    def frequencySort0(self, s):
        if s is None or 0 == len(s):
            return s
        return ''.join([c * cnt for c, cnt in sorted(Counter(s).items(), key=lambda t: t[1], reverse=True)])

    #   https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3337
    #   runtime; 36ms, 87.55%
    #   memory; 14.9MB
    def frequencySort(self, s: str) -> str:
        return ''.join(c * cnt for c, cnt in sorted(Counter(s).items(), key=lambda t: -t[1]))


s = Solution()
data = [('tree', 'eert'),
        ('cccaaa', 'cccaaa'),
        ('Aabb', 'bbAa'),
        ]
for _s, expected in data:
    real = s.frequencySort(_s)
    print('{}, expected {}, real {}, result {}'.format(_s, expected, real, expected == real))
