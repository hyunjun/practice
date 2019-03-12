#   https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree


def height(root):
    if root is None:
        return 0
    depth, q = 0, [(0, root)]
    while q:
        d, node = q.pop(0)
        depth = max(depth, d)
        if node.left:
            q.append((d + 1, node.left))
        if node.right:
            q.append((d + 1, node.right))
    return depth
