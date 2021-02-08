#   https://leetcode.com/problems/serialize-and-deserialize-binary-tree


from TreeNode import TreeNode


#   Runtime Error; OverflowError: cannot fit 'int' into an index-sized integer
class Codec0:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        #   1. get height
        #   2. get the number of all tree nodes = 2^0 + 2^1 + ... + 2^(height - 1) = 2^height - 1
        #   3. traverse tree and set the element's position

        def getHeight(node):
            if node is None:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))

        height = getHeight(root)
        tot = 2 ** height - 1
        l = ['x'] * tot
        q = [(root, 0)]
        while q:
            node, pos = q.pop(0)
            l[pos] = str(node.val)
            if node.left:
                q.append((node.left, pos * 2 + 1))
            if node.right:
                q.append((node.right, pos * 2 + 2))
        return '.'.join(l)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data is None or 0 == len(data):
            return None
        l = [TreeNode(int(val)) if val != 'x' else None for val in data.split('.')]
        for i, node in enumerate(l):
            if node is None:
                continue
            lIdx, rIdx = i * 2 + 1, i * 2 + 2
            if lIdx < len(l):
                node.left = l[i * 2 + 1]
            if rIdx < len(l):
                node.right = l[i * 2 + 2]
        return l[0]


#   Runtime: 128ms, 68.18%
#   Memory: 14.7MB, 21.66%
class Codec:

    def serialize(self, root):
        if root is None:
            return ''
        d, q = {}, [(root, 0)]
        while q:
            node, pos = q.pop(0)
            d[pos] = node.val
            if node.left:
                q.append((node.left, pos * 2 + 1))
            if node.right:
                q.append((node.right, pos * 2 + 2))
        return '.'.join(['{}:{}'.format(pos, val) for pos, val in d.items()])

    def deserialize(self, data):
        if data is None or 0 == len(data):
            return None
        d = {int(item.split(':')[0]):TreeNode(int(item.split(':')[1])) for item in data.split('.')}
        for pos in d.keys():
            lIdx, rIdx = pos * 2 + 1, pos * 2 + 2
            if lIdx in d:
                d[pos].left = d[lIdx]
            if rIdx in d:
                d[pos].right = d[rIdx]
        return d[0]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
codec = Codec()
print(codec.deserialize(codec.serialize(root)))
