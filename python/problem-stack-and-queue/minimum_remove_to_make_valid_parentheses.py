#   https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses


class Solution(object):
    #   runtime; 148ms, 86.80%
    #   memory; 14.6MB, 100.00%
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, removals = [], []
        for i, c in enumerate(s):
            if '(' == c:
                stack.append(i)
            elif ')' == c:
                if 0 == len(stack):
                    removals.append(i)
                else:
                    stack.pop()
            else:
                continue
        l = list(s)
        for i in stack:
            l[i] = ''
        for i in removals:
            l[i] = ''
        return ''.join(l)


solution = Solution()
data = [("lee(t(c)o)de)", "lee(t(c)o)de"),
        ("a)b(c)d", "ab(c)d"),
        ("))((", ""),
        ("(a(b(c)d)", "a(b(c)d)"),
        ]
for s, expected in data:
    real = solution.minRemoveToMakeValid(s)
    print(f'{s}, expected {expected}, real {real}, result {expected == real}')
