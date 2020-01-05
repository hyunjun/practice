#   https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game


from typing import List


class Solution:
    #   runtime; 32ms, 49.88%
    #   memory; 12.7MB, 100.00%
    def tictactoe(self, moves: List[List[int]]) -> str:
        if moves is None or not (1 <= len(moves) <= 9):
            return ''
        grid = [[' '] * 3 for _ in range(3)]
        for i, move in enumerate(moves):
            grid[move[0]][move[1]] = 'X' if i % 2 == 0 else 'O'

        winner = ['A', 'B']
        for i, xo in enumerate(['X', 'O']):
            for r in range(3):
                if all(grid[r][c] == xo for c in range(3)):
                    return winner[i]
            for c in range(3):
                if all(grid[r][c] == xo for r in range(3)):
                    return winner[i]
            if all(grid[i][i] == xo for i in range(3)):
                return winner[i]
            if all(grid[i][2 - i] == xo for i in range(3)):
                return winner[i]

        '''
        for r in range(3):
            if all(grid[r][c] == 'X' for c in range(3)):
                return 'A'
            if all(grid[r][c] == 'O' for c in range(3)):
                return 'B'
        for c in range(3):
            if all(grid[r][c] == 'X' for r in range(3)):
                return 'A'
            if all(grid[r][c] == 'O' for r in range(3)):
                return 'B'
        if all(grid[i][i] == 'X' for i in range(3)):
            return 'A'
        if all(grid[i][i] == 'O' for i in range(3)):
            return 'B'
        if all(grid[i][2 - i] == 'X' for i in range(3)):
            return 'A'
        if all(grid[i][2 - i] == 'O' for i in range(3)):
            return 'B'
        '''
        return 'Draw' if len(moves) == 9 else 'Pending'


s = Solution()
data = [([[0,0],[2,0],[1,1],[2,1],[2,2]], "A"),
        ([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]], "B"),
        ([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]], "Draw"),
        ([[0,0],[1,1]], "Pending"),
        ]
for moves, expected in data:
    real = s.tictactoe(moves)
    print(f'{moves} expected {expected} real {real} result {expected == real}')
