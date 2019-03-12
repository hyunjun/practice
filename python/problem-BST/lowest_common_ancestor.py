#   https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor


def lca(root, v1, v2):
    if root is None:
        return None
    q, pDict, n1, n2 = [(None, root)], {}, None, None
    while q:
        parent, node = q.pop(0)
        if v1 == v2 == node.info:
            return node
        if v1 == node.info:
            n1 = node
        if v2 == node.info:
            n2 = node
        pDict[node] = parent
        if node.left:
            q.append((node, node.left))
        if node.right:
            q.append((node, node.right))
    v1Parents = set([n1])
    n = n1
    while n:
        p = pDict[n]
        v1Parents.add(p)
        n = p
    n = n2
    while n:
        p = pDict[n]
        if p in v1Parents:
            return p
        n = p
    return None
