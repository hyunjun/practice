#   https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree


from TreeNode import TreeNode


class Solution:
    #   runtime; 36ms, 100.00%
    #   memory; 13MB, 100.00%
    def bstToGst0(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        def changeValue(node, val):
            ret = 0
            if node.right:
                ret = changeValue(node.right, val)
            else:
                ret = val
            node.val += ret
            ret = node.val
            if node.left:
                ret = changeValue(node.left, node.val)
            return ret

        changeValue(root, 0)
        return root

    #   runtime; 36ms, 100.00%
    #   memory; 13.2MB, 100.00%
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        prevVal, n, stack = 0, root, []
        while n or stack:
            if n:
                stack.append(n)
                n = n.right
            else:
                n = stack.pop()
                n.val += prevVal
                prevVal = n.val
                n = n.left

        return root


s = Solution()
root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.left.right.right = TreeNode(3)
root.right.right.right = TreeNode(8)
print(root)
print(s.bstToGst(root))
