#   https://leetcode.com/problems/alphabet-board-path


class Solution:
    #   runtime; 36ms, 75.59%
    #   memory; 13.9MB, 100.00%
    def alphabetBoardPath(self, target: str) -> str:
        if target is None or 0 == len(target):
            return ''
        board = {chr(ord('a') + i): (i // 5, i % 5) for i in range(26)}
        p, ans = 'a', []
        for c in target:
            y, x = board[c][0] - board[p][0], board[c][1] - board[p][1]
            lr = 'R' if 0 < x else 'L'
            ud = 'D' if 0 < y else 'U'
            if c == 'z':
                [ans.append(lr) for _ in range(abs(x))]
                [ans.append(ud) for _ in range(abs(y))]
            else:
                [ans.append(ud) for _ in range(abs(y))]
                [ans.append(lr) for _ in range(abs(x))]
            ans.append('!')
            p = c
        return ''.join(ans)


s = Solution()
data = [('leet', 'DDR!UURRR!!DDD!'),
        ('code', 'RR!DDRR!UUL!R!'),
        ('zb', 'DDDDD!UUUUUR!'),
        ('bz', 'R!LDDDDD!'),
        ]
for target, expected in data:
    real = s.alphabetBoardPath(target)
    print(f'{target}, expected {expected}, real {real}, result {expected == real}')
