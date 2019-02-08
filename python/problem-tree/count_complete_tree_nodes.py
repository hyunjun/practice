#   https://leetcode.com/problems/count-complete-tree-nodes


from TreeNode import TreeNode

class Solution:
    #   runtime; 140ms, 30.32%
    #   memory; 15.2MB, 66.50%
    def countNodes(self, root):
        if root is None:
            return 0
        cnt, q = 0, [root]
        while q:
            node = q.pop(0)
            cnt += 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return cnt


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
print(s.countNodes(root))
