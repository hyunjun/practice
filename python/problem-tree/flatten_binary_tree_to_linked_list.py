#   https://leetcode.com/problems/flatten-binary-tree-to-linked-list


from TreeNode import TreeNode


class Solution(object):
    #   50.26%
    def flatten0(self, node):
        if node is None:
            return None
        if node.left is None:
            return self.flatten(node.right)
        if node.right is not None:
            rightmostOfLeft = node.left
            while rightmostOfLeft.right is not None:
                rightmostOfLeft = rightmostOfLeft.right
            rightmostOfLeft.right = node.right
            node.right = None
        node.right = node.left
        node.left = None
        return self.flatten(node.right)

    #   runtime; 40ms, 53.89%
    #   memory; 15.2MB, 75.77%
    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return None

        self.nodes = []
        def preorder(n):
            if n is None:
                return
            self.nodes.append(n)
            if n.left:
                preorder(n.left)
            if n.right:
                preorder(n.right)

        preorder(root)

        for i, node in enumerate(self.nodes):
            node.left, node.right = None, None
            if i == 0:
                continue
            self.nodes[i - 1].right = node


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)
print(root)
s = Solution()
s.flatten(root)
print(root)
