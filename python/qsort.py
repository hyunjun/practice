
def qsort(l):
	if len(l) == 0:	return	[]
	pivot = l[-1:][0]
	left = [ i for i in l[:-1] if i <= pivot ]
	right = [ i for i in l[:-1] if pivot < i ]
	left = qsort(left)
	right = qsort(right)
	left.append(pivot)
	left.extend(right)
	return	left

if __name__ == '__main__':
	l = [ 3, 2, 1, 9, 4, 10, 7 ]
	#pivot = l[-1:][0]
	#left = [ i for i in l[:-1] if i <= pivot ]
	#right = [ i for i in l[:-1] if pivot < i ]
	#print pivot
	#print left
	#print right
	#left.append(pivot)
	#print left + right
	print	qsort(l)
	print	sorted(l)
