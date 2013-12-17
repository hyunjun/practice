if __name__ == '__main__':
	target = 3
	left = target / 2.0
	right = target / 4.0 * 3

	answer = right
	squared = answer * answer
	while abs(squared - target) > 0.001:
		print "%d, estimation %f, squared %f, squared - target %f" % (target, answer, squared, squared - target)
		if abs(target - left * left) < abs(target - right * right):
			right = (left + right) / 2.0
			answer = right
		else:
			left = (left + right) / 2.0
			answer = left
		squared = answer * answer
	print "%d, answer %f, squared %f, squared - target %f" % (target, answer, squared, squared - target)
