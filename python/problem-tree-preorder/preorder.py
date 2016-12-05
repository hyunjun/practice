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

stack = []
cur = root
stack.append(cur)

while 0 < len(stack):
    cur = stack.pop()
    print cur.data
    if cur.right is not None:
        stack.append(cur.right)
    if cur.left is not None:
        stack.append(cur.left)
