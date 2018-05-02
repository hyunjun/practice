import array

class Node(object):
	def __init__(self):
		self.d = []	#	data
		self.v = []	#	data valid
		self.n = []	#	next node
		for i in range(26):	#	use only lowercase alphabet as data
			self.d.append(None)
			self.v.append(False)
			self.n.append(None)
	def printNode(self, prefix=''):
		for i, nn in enumerate(self.n):
			if self.v[i]:
				print '%s%s' % (prefix, self.d[i])
			if nn is not None:
				nn.printNode(prefix+self.d[i])

class SuffixTree(object):
	def __init__(self):
		self.ROOT = Node()
	def pos(self, c):
		return	ord(c)-97
	def add(self, s):
		n = self.ROOT
		for c in s[:-1]:
			p = self.pos(c)
			if n.d[p] is None:
				n.d[p] = c
			if n.n[p] is None:
				n.n[p] = Node()
			n = n.n[p]
		p = self.pos(s[-1])
		if n.d[p] is None:
			n.d[p] = s[-1]
		n.v[p] = True
	def printTree(self):
		print '\n\n[all tree nodes]'
		self.ROOT.printNode()
	def autocomplete(self, inp=''):
		if inp is None or 0 == len(inp):
			while True:
				inp = raw_input('Please type the prefix of a word:')
				self.autocomplete(inp)
		length = len(inp)
		def _pr(n, inp, prefix=''):
			if inp is None or 0 == len(inp):
				for p, vv in enumerate(n.v):
					if vv:
						print '%s%s' % (prefix, n.d[p])
					if n.n[p] is not None:
						_pr(n.n[p], None, prefix=prefix+n.d[p])
			else:
				p = self.pos(inp[0])
				if length <= len(prefix)+1 and n.v[p]:
					print '%s%s' % (prefix, n.d[p])
				_pr(n.n[p], inp[1:], prefix=prefix+n.d[p])
		_pr(self.ROOT, inp)

if __name__ == '__main__':
	suffixTree = SuffixTree()
	with open('data.txt', 'r') as f:
		[ suffixTree.add(l.strip()) for l in f.readlines() ]
	suffixTree.printTree()
	for s in ['ab', 'br']:
		print '\n\n[prefix %s]' % s
		suffixTree.autocomplete(s)
	#suffixTree.autocomplete()
