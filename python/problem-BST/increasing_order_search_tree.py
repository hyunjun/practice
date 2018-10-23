#   https://leetcode.com/problems/increasing-order-search-tree

#   https://leetcode.com/problems/increasing-order-search-tree/solution


from TreeNode import TreeNode


class Solution:
    #   Could NOT submit because there is a weird test case such as below;
    #   [379
    #    826]
    def increasingBST0(self, root):
        if root is None:
            return None
        cur, stack, res = root, [], []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if cur:
                    res.append(cur)
                    cur = cur.right
        for i, r in enumerate(res):
            if 0 == i:
                continue
            res[i - 1].left = None
            res[i - 1].right = r
        return res[0]

    def increasingBST(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right


s = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)
print(s.increasingBST(root))
