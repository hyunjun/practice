#   https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses


class Solution(object):
    #   runtime; 148ms, 86.80%
    #   memory; 14.6MB, 100.00%
    def minRemoveToMakeValid0(self, s):
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

    #   https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3645
    #   runtime; 172ms, 26.70%
    #   memory; 25.1MB
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, positions = [], set()
        for i, c in enumerate(s):
            if c == ')':
                if 0 < len(stack) and stack[-1][0] == '(':
                    _, oi = stack.pop()
                    positions.add(oi)
                    positions.add(i)
            elif c == '(':
                stack.append((c, i))
            else:
                positions.add(i)
        return ''.join(c for i, c in enumerate(s) if i in positions)


solution = Solution()
data = [("lee(t(c)o)de)", "lee(t(c)o)de"),
        ("a)b(c)d", "ab(c)d"),
        ("))((", ""),
        ("(a(b(c)d)", "a(b(c)d)"),
        ]
for s, expect in data:
    real = solution.minRemoveToMakeValid(s)
    print(f'{s}, expect {expect}, real {real}, result {expect == real}')
