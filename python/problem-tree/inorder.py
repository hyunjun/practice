#   https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.visited = False
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


def inorder_recur(node, res):
    if node is None:
        return
    inorder_recur(node.left, res)
    res.append(node.val)
    inorder_recur(node.right, res)


def inorder(node):
    cur, stack, res = node, [], []
    while cur is not None or 0 < len(stack):
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
    return res


if __name__ == '__main__':
    res = []
    inorder_recur(root, res)
    print(res)
    print(inorder(root))
