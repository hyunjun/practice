
RIGHT=1
DOWN=RIGHT<<1
LEFT=DOWN<<1
UP=LEFT<<1
def next_dir(direction):
	if direction == UP:	return	RIGHT
	return	direction<<1

def move(matrix, visited, direction, r, c):
	if visited[r][c]:	return
	print 'matrix[%d][%d] = %d' % (r, c, matrix[r][c])
	visited[r][c] = True
	if direction == RIGHT:
		if c + 1 < len(matrix[0]) and visited[r][c+1] == False:
			move(matrix, visited, direction, r, c + 1)
		else:
			move(matrix, visited, next_dir(direction), r + 1, c)
	if direction == DOWN:
		if r + 1 < len(matrix) and visited[r+1][c] == False:
			move(matrix, visited, direction, r + 1, c)
		else:
			move(matrix, visited, next_dir(direction), r, c - 1)
	if direction == LEFT:
		if 0 <= c - 1 and visited[r][c-1] == False:
			move(matrix, visited, direction, r, c - 1)
		else:
			move(matrix, visited, next_dir(direction), r - 1, c)
	if direction == UP:
		if 0 <= r - 1 and visited[r-1][c] == False:
			move(matrix, visited, direction, r - 1, c)
		else:
			move(matrix, visited, next_dir(direction), r, c + 1)

if __name__ == '__main__':
	matrix = [ [ 1, 2, 3, 4 ],
			[ 5, 6, 7, 8 ],
			[ 9, 10, 11, 12 ],
			[ 13, 14, 15, 16 ] ]
	visitedR = [ False, False, False, False ]
	visited = [ list(visitedR), list(visitedR), list(visitedR), list(visitedR) ]
	for m in matrix:
		for mi in m:
			print mi,
		print
	for v in visited:
		for vi in v:
			print vi,
		print
	move(matrix, visited, RIGHT, 0, 0)
