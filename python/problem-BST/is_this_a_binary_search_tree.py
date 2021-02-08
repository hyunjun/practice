#   https://www.hackerrank.com/challenges/ctci-is-binary-search-tree

#   http://www.ardendertat.com/2011/10/10/programming-interview-questions-7-binary-search-tree-check


def checkBST(root):

    def isBST(node, _min, _max):
        if node is None or node.left is None and node.right is None and _min < node.data < _max:
            return True
        if node.left and node.left.data >= node.data or node.right and node.right.data <= node.data or node.data <= _min or _max <= node.data:
            return False
        return isBST(node.left, _min, node.data) and isBST(node.right, node.data, _max)

    return isBST(root, -float('inf'), float('inf'))


def checkBST(root):
    q = [(-float('inf'), root, float('inf'))]
    while q:
        _min, node, _max = q.pop(0)
        if node.data <= _min or _max <= node.data:
            return False
        if node.left:
            q.append((_min, node.left, node.data))
        if node.right:
            q.append((node.data, node.right, _max))
    return True
