from TreeNode import TreeNode
from inorder import root


def preorder_recur(node, res):
    if node is None:
        return
    res.append(node.val)
    preorder_recur(node.left, res)
    preorder_recur(node.right, res)


def preorder(node):
    stack, res = [node], []
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return res


if __name__ == '__main__':
    res = []
    preorder_recur(root, res)
    print(res)
    print(preorder(root))
