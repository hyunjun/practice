#   https://www.hackerrank.com/challenges/swap-nodes-algo


from TreeNode import TreeNode


def construct(indexes):
    head = TreeNode(1)
    q = [head]
    for lVal, rVal in indexes:
        n = q.pop(0)
        if -1 != lVal:
            n.left = TreeNode(lVal)
            q.append(n.left)
        if -1 != rVal:
            n.right = TreeNode(rVal)
            q.append(n.right)
    return head


def inorder(node):
    res = []
    def _inorder(n):
        if n:
            _inorder(n.left)
            res.append(n.val)
            _inorder(n.right)
    _inorder(node)
    return res


def swapNodes(indexes, queries):
    res, head = [], construct(indexes)
    for query in queries:
        q = [(1, head)]
        while q:
            d, n = q.pop(0)
            if d % query == 0:
                n.left, n.right = n.right, n.left
            if n.left:
                q.append((d + 1, n.left))
            if n.right:
                q.append((d + 1, n.right))
        res.append(inorder(head))
    return res


data = [([[2, 3], [-1, -1], [-1, -1]], [1, 1]),
        ([[2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], [10, 11], [12, 13], [-1, 14], [-1, -1], [15, -1], [16, 17], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]], [2, 3]),
        ([[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]], [2, 4]),
        ]
for indexes, queries in data:
    for r in swapNodes(indexes, queries):
        print(r)
