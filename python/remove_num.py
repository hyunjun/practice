
def remove_num(array, num):
	if array is None or len(array) == 0:
		return	None

	c = r = len(array) - 1
	while True:
		while array[c] != num:
			c -= 1
		if c < 0:	break
		print "before swap %s, cur[%d]=%d, remove[%d]=%d" % (array, c, array[c], r, array[r])
		array[c] = array[r]
		array[r] = num
		print " after swap %s, cur[%d]=%d, remove[%d]=%d" % (array, c, array[c], r, array[r])
		c -= 1
		r -= 1
	return	array[:r+1]

if __name__ == '__main__':
	array = [ 4, 3, 2, 1, 2, 3, 6 ]
	print array
	print remove_num(array, 2)
