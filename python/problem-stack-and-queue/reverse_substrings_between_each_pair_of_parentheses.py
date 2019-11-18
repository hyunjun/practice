#   https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses


class Solution(object):
    #   runtime; 20ms, 65.03%
    #   memory; 11.8MB, 100.00%
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res, stack = [], []
        for c in s:
            if '(' == c:
                stack.append(c)
            elif ')' == c:
                tmp = []
                while stack[-1] != '(':
                    tmp.append(stack.pop())
                stack.pop()
                if len(stack) == 0:
                    res.extend(tmp)
                else:
                    stack.extend(tmp)
            else:
                if len(stack) == 0:
                    res.append(c)
                else:
                    stack.append(c)
        return ''.join(res)


solution = Solution()
data = [("(abcd)", "dcba"),
        ("(u(love)i)", "iloveu"),
        ("(ed(et(oc))el)", "leetcode"),
        ("a(bcdefghijkl(mno)p)q", "apmnolkjihgfedcbq"),
        ]
for s, expected in data:
    real = solution.reverseParentheses(s)
    print(f'{s}, expected {expected}, real {real}, result {expected == real}')
