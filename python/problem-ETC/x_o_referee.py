#   https://py.checkio.org/mission/x-o-referee


from typing import List

def checkio(game_result):
    for r in range(3):
        rowSet = set([game_result[r][c] for c in range(3)])
        if set(['O']) == rowSet:
            return 'O'
        if set(['X']) == rowSet:
            return 'X'
    for c in range(3):
        colSet = set([game_result[r][c] for r in range(3)])
        if set(['O']) == colSet:
            return 'O'
        if set(['X']) == colSet:
            return 'X'
    diagonalSet = set([game_result[i][i] for i in range(3)])
    if set(['O']) == diagonalSet:
        return 'O'
    if set(['X']) == diagonalSet:
        return 'X'
    diagonalSet = set([game_result[2 - i][i] for i in range(3)])
    if set(['O']) == diagonalSet:
        return 'O'
    if set(['X']) == diagonalSet:
        return 'X'
    return 'D'


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
