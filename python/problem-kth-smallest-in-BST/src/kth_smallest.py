
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __repr__(self):
        return '[{}]'.format(self.data)


#   http://www.programcreek.com/2014/07/leetcode-kth-smallest-element-in-a-bst-java/
def kth_smallest(root, k):
    stack = []
    result = None
    node = root
    while 0 < len(stack) or node is not None:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            popped = stack[-1]
            del stack[-1]
            k -= 1
            if k == 0:
                result = popped.data
            node = popped.right
    return result


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.right = Node(16)
    root.left.left = Node(3)
    root.left.right = Node(7)
    print kth_smallest(root, 3)
