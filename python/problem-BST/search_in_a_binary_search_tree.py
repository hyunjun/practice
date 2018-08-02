#   https://leetcode.com/problems/search-in-a-binary-search-tree


from TreeNode import TreeNode


class Solution:
    #   0.0%?
    def searchBST(self, root, val):
        if root is None:
            return None
        cur = root
        while cur:
            if cur.val == val:
                return cur
            if cur.val < val:
                cur = cur.right
            else:
                cur = cur.left
        return None


s = Solution()

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
print(s.searchBST(root, 2))
print(s.searchBST(root, 5))
