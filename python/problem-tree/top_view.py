#   https://www.hackerrank.com/challenges/tree-top-view


def topView(root):
    q, d = [(0, 0, root)], {}
    while q:
        x, y, n = q.pop(0)
        if x in d:
            if y < d[x][0]:
                d[x] = (y, n.info)
        else:
            d[x] = (y, n.info)
        if n.left:
            q.append((x - 1, y + 1, n.left))
        if n.right:
            q.append((x + 1, y + 1, n.right))
    return ' '.join([str(t[1]) for _, t in sorted(d.items(), key=lambda t: t[0])])
