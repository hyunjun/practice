#   https://leetcode.com/problems/reverse-words-in-a-string-iii

#   https://leetcode.com/problems/reverse-words-in-a-string-iii/solution


class Solution:
    #   6.63%
    def reverseWords(self, s):
        if s is None or 0 == len(s):
            return s
        l = list(s)
        s, e = 0, 0
        for i in range(len(l)):
            if ' ' == l[i]:
                e = i - 1
                while s < e:
                    l[s], l[e] = l[e], l[s]
                    s += 1
                    e -= 1
                s = i + 1
        e = len(l) - 1
        while s < e:
            l[s], l[e] = l[e], l[s]
            s += 1
            e -= 1
        return ''.join(l)


solution = Solution()
data = [("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
        ]
for s, expected in data:
    real = solution.reverseWords(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
