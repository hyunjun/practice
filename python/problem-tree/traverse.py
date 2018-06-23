class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(6)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.left.left.left = Node(1)
root.left.right.right = Node(5)
root.right.right = Node(9)


def pre(node):
    def _pre(node):
        if node is not None:
            print(node.data,)
            _pre(node.left)
            _pre(node.right)
    _pre(node)
    print


def inorder(node):
    def _in(node):
        if node is not None:
            _in(node.left)
            print(node.data,)
            _in(node.right)
    _in(node)
    print


def post(node):
    def _post(node):
        if node is not None:
            _post(node.left)
            _post(node.right)
            print(node.data,)
    _post(node)
    print


def level(node):
    queue = []
    queue.append(node)
    while 0 < len(queue):
        cur = queue[0]
        queue.remove(cur)
        print(cur.data,)
        if cur.left is not None:
            queue.append(cur.left)
        if cur.right is not None:
            queue.append(cur.right)


print('pre order')
pre(root)
print('in order')
inorder(root)
print('post order')
post(root)
print('level order')
level(root)
