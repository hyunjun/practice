import sys

def isPalindrome(num):
	if num is None:
		return	False
	try:
		int(num)
	except ValueError:
		return	False

	l, r = 0, len(num)
	while l <= r:
		if num[l:l+1] != num[r-1:r]:
			return	False
		l += 1
		r -= 1
	return	True

def isPalindrome2(num):
	if num is None:	return	False
	try:
		int(num)
	except ValueError:
		return	False
	return	num == num[::-1]

if __name__ == '__main__':
	input = sys.argv[1]
	print isPalindrome(input)
	print isPalindrome2(input)
