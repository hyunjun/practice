from inorder import TreeNode
from inorder import root


def levelorder(node):
    queue, res = [node], []
    while queue:
        cur = queue[0]
        del queue[0]
        res.append(cur.val)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return res


if __name__ == '__main__':
    print(levelorder(root))
