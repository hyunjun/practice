#   https://leetcode.com/problems/complete-binary-tree-inserter

#   https://leetcode.com/problems/complete-binary-tree-inserter/solution


from TreeNode import TreeNode

#   runtime; 720ms, 7.01%
#   memory; 13.2MB, 100.00%
class CBTInserter:

    def __init__(self, root):
        self.root = root

    def insert(self, v):
        q = [self.root]
        while q:
            node = q.pop(0)
            if node.left is None:
                node.left = TreeNode(v)
                return node.val
            elif node.right is None:
                node.right = TreeNode(v)
                return node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return 0

    def get_root(self):
        return self.root


c = CBTInserter(TreeNode(1))
print(c.insert(2))
print(c.get_root())

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
c = CBTInserter(root)
print(c.insert(7))
print(c.insert(8))
print(c.get_root())
