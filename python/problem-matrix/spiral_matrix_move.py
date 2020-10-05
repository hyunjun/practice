'''
## Print a Spiral
/*
Implement a function that prints a spiral
// Input:
print_spiral(3)
// Output:
1 1 1
0 0 1
0 1 1
// Input:
print_spiral(4)
// Output:
1 1 1 1
0 0 0 1
0 1 0 1
0 1 1 1
// Input:
print_spiral(5)
// Output:
1 1 1 1 1
0 0 0 0 1
0 1 1 0 1
0 1 0 0 1
0 1 1 1 1
// Input:
print_spiral(6)
// Output:
1 1 1 1 1 1
0 0 0 0 0 1
0 1 1 1 0 1
0 1 0 1 0 1
0 1 0 0 0 1
0 1 1 1 1 1

direction = right -> down -> left -> up -> right -> ...
cnt = N -> N - 1 -> N - 2 -> ...
'''

SIZE = 5
boards = [[0] * SIZE for _ in range(SIZE)]
RIGHT, DOWN, LEFT, UP = 2, 4, 8, 1

def fill(boards, direction, cnt, r, c):
    if cnt == 0:
        for b in boards:
            print(b)
        return
    if direction == RIGHT:
        end = c + cnt
        while c < end:
            boards[r][c] = 1
            c += 1
        fill(boards, DOWN, cnt - 1, r + 1, c - 1)
    elif direction == DOWN:
        end = r + cnt
        while r < end:
            boards[r][c] = 1
            r += 1
        fill(boards, LEFT, cnt - 1, r - 1, c - 1)
    elif direction == LEFT:
        end = c - cnt
        while end < c:
            boards[r][c] = 1
            c -= 1
        fill(boards, UP, cnt - 1, r - 1, c + 1)
    elif direction == UP:
        end = r - cnt
        while end < r:
            boards[r][c] = 1
            r -=1
        fill(boards, RIGHT, cnt - 1, r + 1, c + 1)

for b in boards:
    print(b)
fill(boards, RIGHT, SIZE, 0, 0)
