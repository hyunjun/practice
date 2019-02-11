#   https://leetcode.com/problems/insert-into-a-binary-search-tree


from TreeNode import TreeNode

class Solution:
    #   runtime; 120ms, 96.12%
    #   memory; 10MB, 67.05%
    def insertIntoBST(self, root, val):
        if root is None:
            return None
        node = root
        while node:
            parent = node
            if node.val < val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
            elif val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
        return root


s = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(s.insertIntoBST(root, 5))
