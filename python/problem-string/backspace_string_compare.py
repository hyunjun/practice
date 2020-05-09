#   https://leetcode.com/problems/backspace-string-compare

#   https://leetcode.com/problems/backspace-string-compare/solution


class Solution:
    #   66.82%
    def backspaceCompare0(self, S, T):
        def applyBackspace(s):
            i, stack = 0, []
            while i < len(s):
                if '#' == s[i]:
                    if stack:
                        stack.pop()
                else:
                    stack.append(s[i])
                i += 1
            return ''.join(stack)

        return applyBackspace(S) == applyBackspace(T)

    #   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3291
    #   runtime; 20ms, 98.37%
    #   memory; 13.9MB
    def backspaceCompare1(self, S: str, T: str) -> bool:
        if (S is None and T) or (S and T is None) or S == T:
            return True
        if S is None or T is None or not (1 <= len(S) <= 200) or not (1 <= len(T) <= 200):
            return False

        def remove(s):
            l, c = list(s), 0
            for i in range(len(s) - 1, -1, -1):
                if l[i] == '#':
                    c += 1
                else:
                    if 0 < c:
                        l[i] = None
                        c -= 1
            return [c for c in l if c and 'a' <= c <= 'z']

        return remove(S) == remove(T)

    #   runtime; 28ms, 71.87%
    #   memory; 13.9MB, 8.00%
    def backspaceCompare(self, S: str, T: str) -> bool:
        if not (1 <= len(S) <= 200) or not (1 <= len(T) <= 200):
            return False
        
        def backspaced(s):
            stack = []
            for c in s:
                if c == '#':
                    if 0 < len(stack):
                        stack.pop()
                else:
                    stack.append(c)
            return ''.join(stack)
        
        return backspaced(S) == backspaced(T)


s = Solution()
data = [('ab#c', 'ad#c', True),
        ('ab##', 'c#d#', True),
        ('a##c', '#a#c', True),
        ('a#c', 'b', False),
        ]
for S, T, expected in data:
    real = s.backspaceCompare(S, T)
    print(f'{S}, {T}, expected {expected}, real {real}, result {expected == real}')
