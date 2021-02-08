#   https://leetcode.com/problems/invert-binary-tree

#   https://leetcode.com/problems/invert-binary-tree/solution


from TreeNode import TreeNode


class Solution:

    #   44.59% O(n), O(n)
    def invertTree0(self, root):
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    #   https://leetcode.com/explore/featured/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3347
    #   runtime; 36ms, 20.12%
    #   memory; 13.8MB
    def invertTree1(self, root: TreeNode) -> TreeNode:

        def invert(node):
            if node is None:
                return None
            node.left, node.right = invert(node.right), invert(node.left)
            return node

        return invert(root)

    #   runtime; 28ms, 75.61%
    #   memory; 13.8MB
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        q = [root]
        while q:
            n = q.pop(0)
            n.left, n.right = n.right, n.left
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return root


'''
     4
   /   \
  2     7
 / \   / \
1   3 6   9

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
print(root)

s = Solution()
print(s.invertTree(root))
