#   https://leetcode.com/problems/binary-tree-right-side-view

#   https://leetcode.com/problems/binary-tree-right-side-view/solution


from TreeNode import TreeNode


class Solution:
    #   100.00%
    def rightSideView(self, root):
        if root is None:
            return []
        res, queue = [], [(root, 0)]
        while queue:
            cur, depth = queue.pop(0)
            if len(res) == depth:
                res.append(cur.val)
            else:
                res[depth] = cur.val
            if cur.left:
                queue.append((cur.left, depth + 1))
            if cur.right:
                queue.append((cur.right, depth + 1))
        return res


s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
print(s.rightSideView(root) == [1, 3, 4])

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
print(s.rightSideView(root) == [1, 3, 5])
