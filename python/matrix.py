if __name__ == '__main__':
	nums = [ [ 1, 3, 5 ], [ 7, 9, 11 ], [ 13, 15, 17 ] ]
	target = 5
	for line in nums:
		if target in line:
			print line

	nums = [ [ 1, 2, 8, 9 ], [ 2, 4, 9, 12 ], [ 4, 7, 10, 13 ], [ 6, 8, 11, 15 ] ]
	row = 0
	col = len(nums[row]) - 1
	print 'start row %d, col %d' % (row, col)
	while row < len(nums) and 0 <= col:
		print 'nums[%d][%d] = %d' % (row, col, nums[row][col])
		if nums[row][col] == target:
			print 'found'
			break
		elif nums[row][col] > target:
			col -= 1
		else:	#if nums[row][col] < target:
			row += 1
