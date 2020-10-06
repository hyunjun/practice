#   https://leetcode.com/problems/insert-into-a-binary-search-tree


from TreeNode import TreeNode


class Solution:
    #   runtime; 120ms, 96.12%
    #   memory; 10MB, 67.05%
    def insertIntoBST0(self, root, val):
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

    #   https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3485
    #   runtime; 128ms, 97.86%
    #   memory; 16.3MB, 11.15%
    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val)

        def insert(node):
            if node.val < val:
                if node.right:
                    insert(node.right)
                else:
                    node.right = TreeNode(val)
            elif val < node.val:
                if node.left:
                    insert(node.left)
                else:
                    node.left = TreeNode(val)

        insert(root)
        return root


s = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(s.insertIntoBST(root, 5))
