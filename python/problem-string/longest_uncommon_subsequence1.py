#   https://leetcode.com/problems/longest-uncommon-subsequence-i

#   https://leetcode.com/problems/longest-uncommon-subsequence-i/solution


class Solution:
    #   Wrong Answer
    def findLUSlength0(self, a, b):
        def findLength(s1, s2):
            charSet = set(s2)
            s, e, maxLen = -1, -1, -1
            for i, c in enumerate(s1):
                if 0 == i and c not in charSet:
                    s = 0
                else:
                    if s1[i - 1] in charSet and c not in charSet:
                        s = i
                    elif s1[i - 1] not in charSet and c in charSet:
                        e = i - 1
                        maxLen = max(maxLen, e - s + 1)
            if s1[-1] not in charSet:
                maxLen = max(maxLen, len(s1) - s)
            return maxLen

        if a is None or 0 == len(a) or b is None or 0 == len(b):
            return 0
        return max(findLength(a, b), findLength(b, a))

    #   86.97%
    def findLUSlength(self, a, b):
        if a == b:
            return -1
        return max(len(a), len(b))


s = Solution()
data = [('aba', 'cdc', 3),
        ('dabca', 'cdc', 5),
        ('aefawfawfawfaw', 'aefawfeawfwafwaef', 17),
        ]
for a, b, expected in data:
    real = s.findLUSlength(a, b)
    print('{}, {}, expected {}, real {}, result {}'.format(a, b, expected, real, expected == real))
