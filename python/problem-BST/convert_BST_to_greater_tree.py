#   https://leetcode.com/problems/convert-bst-to-greater-tree

#   https://leetcode.com/problems/convert-bst-to-greater-tree/solution


from TreeNode import TreeNode


class Solution:
    #   30.39%
    def convertBST(self, root):
        if root is None:
            return None
        cur, stack, nodes = root, [], []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                nodes.append(cur)
                cur = cur.right
        addition = 0
        for i in range(len(nodes) - 1, -1, -1):
            nodes[i].val += addition
            addition = nodes[i].val
        return root


s = Solution()

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)
print(root)
print(s.convertBST(root))
