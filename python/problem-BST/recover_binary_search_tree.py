#   https://leetcode.com/problems/recover-binary-search-tree


from TreeNode import TreeNode
import sys

class Solution:
    #   Wrong Answer
    def recoverTree0(self, root):
        if root is None:
            return
        #   traverse tree to find the wrong nodes
        #   min < node.val < max
        def isRightNode(node, minNode, maxNode):
            if node is None:
                return
            if minNode.val < node.val < maxNode.val:
                isRightNode(node.left, minNode, node)
                isRightNode(node.right, node, maxNode)
            else:
                if maxNode.val < node.val:
                    node.val, maxNode.val = maxNode.val, node.val
                elif node.val < minNode.val:
                    node.val, minNode.val = minNode.val, node.val

        isRightNode(root, TreeNode(-sys.maxsize), TreeNode(sys.maxsize))

    #   runtime; 124ms, 48.34%
    #   memory; 12.5MB, 100.00%
    def recoverTree(self, root):
        if root is None:
            return
        n, stack, res = root, [], []
        while n or stack:
            if n:
                stack.append(n)
                n = n.left
            else:
                n = stack.pop()
                res.append(n)
                n = n.right
        vals = sorted([r.val for r in res])
        print([r.val for r in res])
        print(vals)
        for i, r in enumerate(res):
            r.val = vals[i]



s = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
print(root1)
s.recoverTree(root1)
print(root1)
root2 = TreeNode(3)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(2)
print(root2)
s.recoverTree(root2)
print(root2)
root3 = TreeNode(2)
root3.left = TreeNode(3)
root3.right = TreeNode(1)
print(root3)
s.recoverTree(root3)
print(root3)
