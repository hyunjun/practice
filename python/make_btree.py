
class Node:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

#	make binary tree from preorder & inorder list
def make_btree(pres, ins):	#	pres = preorder list, ins = inorder list
	def make_btree_r(pres, ins):
		node = Node(pres[:1][0])
		idx = 0
		for i, v in enumerate(ins):
			if v == pres[:1][0]:
				idx = i
				break
		node.left = None
		if 0 < idx:
			node.left = make_btree_r(pres[1:1+idx], ins[:idx])
		node.right = None
		if idx < len(ins) - 1:
			node.right = make_btree_r(pres[1+idx:], ins[idx+1:])
		return	node
	return	make_btree_r(pres, ins)

def print_preorder(node):
	def print_preorder_r(node):
		print node.data,
		if node.left is not None:
			print_preorder_r(node.left)
		if node.right is not None:
			print_preorder_r(node.right)
	print_preorder_r(node)
	print

def print_inorder(node):
	def print_inorder_r(node):
		if node.left is not None:
			print_inorder_r(node.left)
		print node.data,
		if node.right is not None:
			print_inorder_r(node.right)
	print_inorder_r(node)
	print

#	make binary search tree from postorder list
def make_btree2(posts):	#	posts = postorder list
	def make_btree_r(posts):
		node = Node(posts[-1:][0])
	
		lefts = [ n for n in posts if n < posts[-1:][0] ]
		rights = [ n for n in posts if posts[-1:][0] < n ]
		#	TODO:	check all the indices of lefts must smaller than those of rights

		node.left = None
		if len(lefts) > 0:
			node.left = make_btree_r(lefts)
	
		node.rights = None
		if len(rights) > 0:
			node.right = make_btree_r(rights)
		
		return	node
	return	make_btree_r(posts)

def print_postorder(node):
	def print_postorder_r(node):
		if node.left is not None:
			print_postorder_r(node.left)
		if node.right is not None:
			print_postorder_r(node.right)
		print node.data,
	print_postorder_r(node)
	print
if __name__ == '__main__':
	root = make_btree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])

	print_preorder(root)
	print_inorder(root)

	root = make_btree2([5, 7, 6, 9, 11, 10, 8])
	print_postorder(root)
	#root = make_btree2([7, 4, 6, 5])	#	must return None because it's not binary seary tree

