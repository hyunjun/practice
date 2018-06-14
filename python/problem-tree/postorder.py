from TreeNode import TreeNode2


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
    root = TreeNode2(1)
    root.left = TreeNode2(2)
    root.right = TreeNode2(3)
    root.left.left = TreeNode2(4)
    root.left.right = TreeNode2(5)
    res = []
    postorder_recur(root, res)
    print(res)
    print(postorder(root))
