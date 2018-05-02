from inorder import TreeNode
from inorder import root


def postorder_recur(node, res):
    if node is None:
        return
    postorder_recur(node.left, res)
    postorder_recur(node.right, res)
    res.append(node.val)


def postorder(node):
    stack, res = [node], []
    while stack:
        cur = stack.pop()
        if cur.visited:
            if cur.val not in res:
                res.append(cur.val)
        else:
            cur.visited = True
            stack.append(cur)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return res


if __name__ == '__main__':
    res = []
    postorder_recur(root, res)
    print(res)
    print(postorder(root))
