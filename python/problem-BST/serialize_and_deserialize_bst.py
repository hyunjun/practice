#   https://leetcode.com/problems/serialize-and-deserialize-bst
#   2.89%


from TreeNode import TreeNode


class Codec:
    def serialize(self, root):
        if root is None:
            return ''
        res, queue = [], [(root, 0)]
        while queue:
            cur, idx = queue[0]
            del queue[0]
            res.append('{},{}'.format(cur.val, idx))
            if cur.left:
                queue.append((cur.left, 2 * idx + 1))
            if cur.right:
                queue.append((cur.right, 2 * idx + 2))
        return '|'.join(res)

    def deserialize(self, data):
        if data is None or 0 == len(data):
            return None
        d = {}
        for item in data.split('|'):
            val, idx = item.split(',')
            val, idx = int(val), int(idx)
            d[idx] = TreeNode(val)
            if 0 == idx:
                continue
            if 1 == idx % 2:
                d[(idx - 1) // 2].left = d[idx]
            else:
                d[(idx - 2) // 2].right = d[idx]
        return d[0]


root = TreeNode(5)
root.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(9)
root.right.left = TreeNode(7)

codec = Codec()
real = codec.deserialize(codec.serialize(root))
print(root)
print(real)
