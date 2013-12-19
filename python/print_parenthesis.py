
#	http://www.careercup.com/question?id=6234634354425856

def print_parenthesis(n):
	def print_parenthesis_r(s, o, c):	#	s = str, o = # of open, c = # of close
		#print 'start', s, o, c
		if o == 0:
			for i in range(c):
				s += ')'
			print s
		if s[-1:] == '(':
			if 0 < o:
				print_parenthesis_r(s + '(', o-1, c)
			if 0 < c:
				#print s + ')', o, c-1
				print_parenthesis_r(s + ')', o, c-1)
		elif s[-1:] == ')':
			if 0 < o:
				#print s + '(', o-1, c
				print_parenthesis_r(s + '(', o-1, c)
	print_parenthesis_r('(', n-1, n)

if __name__ == '__main__':
	print_parenthesis(2)
	print_parenthesis(3)
