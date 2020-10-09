#   https://leetcode.com/problems/serialize-and-deserialize-bst


from TreeNode import TreeNode


#   2.89%
class Codec0:
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

#   https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3489
#   runtime; 96ms, 38.82%
#   memory; 18.2MB
class Codec:
    def serialize(self, root: TreeNode) -> str:
        def convert(node):
            if node is None:
                return ''
            return '|'.join([str(node.val), convert(node.left), convert(node.right)])
        return convert(root)

    def deserialize(self, data: str) -> TreeNode:
        def convert(arr):
            if 0 == len(arr):
                return None
            node = TreeNode(arr[0])
            node.left, node.right = convert([a for a in arr if a < arr[0]]), convert([a for a in arr if a > arr[0]])
            return node
        return convert([int(d) for d in data.split('|') if d != ''])


root = TreeNode(51)
root.left = TreeNode(32)
root.left.right = TreeNode(43)
root.right = TreeNode(94)
root.right.left = TreeNode(75)

codec = Codec()
print(codec.serialize(root))
real = codec.deserialize(codec.serialize(root))
print(root)
print(real)
