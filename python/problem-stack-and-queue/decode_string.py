#   https://leetcode.com/problems/decode-string


class Solution:
    #   https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3536
    #   runtime; 32ms, 33.43%
    #   memory; 14MB, 70.09%
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                tempStr, tempNum = [], []
                while 0 < len(stack) and stack[-1] != '[':
                    tempStr.append(stack.pop())
                stack.pop()
                while 0 < len(stack) and '0' <= stack[-1] <= '9':
                    tempNum.append(stack.pop())
                stack.append(int(''.join(tempNum[::-1])) * ''.join(tempStr[::-1]))
            else:
                stack.append(c)
        return ''.join(stack)


solution = Solution()
data = [("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("abc3[cd]xyz", "abccdcdcdxyz"),
        ]
for s, expect in data:
    real = solution.decodeString(s)
    print(f'{s} expect {expect} real {real} result {expect == real}')
