#   https://codebasil.com/problems/word-snake


#   Wrong Answer
def wordSnake0(board, word):
    if board is None or 0 == len(board) or 0 == len(board[0]):
        return False
    if word is None or 0 == len(word):
        return True
    R, C = len(board), len(board[0])
  
    def search(r, c, chars):
        q = [(r, c, chars, set())]
        while q:
            n, m, w, s = q.pop(0)
            s.add((n, m))
            print(n, m, w)
            if board[n][m] == w[0]:
                if len(w) == 1:
                    return True
                for nn, nm in [(n + 1, m), (n - 1, m), (n, m + 1), (n, m - 1)]:
                    if 0 <= nn < R and 0 <= nm < C and board[nn][nm] == w[1] and (nn, nm) not in s:
                        q.append((nn, nm, w[1:], s))
        return False
  
    for r in range(R):
        for c in range(C):
            if board[r][c] == word[0]:
                if search(r, c, word):
                    return True
    return False


from collections import defaultdict


def wordSnake(board, word):
    if board is None or 0 == len(board) or 0 == len(board[0]):
        return False
    if word is None or 0 == len(word):
        return True
    d, R, C = defaultdict(list), len(board), len(board[0])
    for r in range(R):
        for c in range(C):
            d[board[r][c]].append([r, c])

    def traverse(visited, remains):
        if 0 == len(remains):
            if len(visited) == len(set(visited)):
                return True
            return False
        for r, c in d[remains[0]]:
            if 0 < len(visited) and not ((abs(visited[-1][0] - r) == 1 and visited[-1][1] == c) or (visited[-1][0] == r and abs(visited[-1][1] - c) == 1)):
                continue
            visited.append((r, c))
            if traverse(visited, remains[1:]):
                return True
            visited.pop()
        return False

    return traverse([], word)


matrix1 = [['E', 'P', 'Y', 'T', 'A'],
           ['Z', 'B', 'R', 'H', 'O'],
           ['A', 'M', 'N', 'O', 'P'],
           ]
data = [(matrix1, 'RYTHOP', True),
        (matrix1, 'PYTHON', True),
        (matrix1, 'MAZE', True),
        (matrix1, 'PYTHORN', False),
        (matrix1, 'POATYPEZAMNOHRB', True),
        (matrix1, 'EPYTAOPONMAZE', False),
        ]
for board, word, expected in data:
    for b in board:
        print(b)
    real = wordSnake(board, word)
    print(f'{word} expected {expected} real {real} result {expected == real}')
