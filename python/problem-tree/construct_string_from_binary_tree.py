#   https://leetcode.com/problems/construct-string-from-binary-tree

#   https://leetcode.com/problems/construct-string-from-binary-tree/solution


from TreeNode import TreeNode


class Solution:
    #   4.53%
    def tree2str(self, t):
        if t is None:
            return ''
        def _preorder(node):
            if node is None:
                return '()'
            if node.left is None and node.right is None:
                return '({})'.format(node.val)
            if node.left and node.right is None:
                return '({}{})'.format(node.val, _preorder(node.left))
            return '({}{}{})'.format(node.val, _preorder(node.left), _preorder(node.right))
        res = _preorder(t)
        return res[1:len(res) - 1]

    #   1.01%
    def tree2strIter(self, t):
        if t is None:
            return ''
        stack, res = [t], []
        while stack:
            cur = stack.pop()
            if '(' == cur:
                res.append(cur)
            if ')' == cur:
                res.append(cur)
                while stack and ')' == stack[-1]:
                    res.append(stack.pop())
            if cur not in ['(', ')']:
                res.append(cur.val)
                if cur.right or cur.left:
                    if cur.right:
                        stack.append(')')
                        stack.append(cur.right)
                        stack.append('(')
                    stack.append(')')
                    if cur.left:
                        stack.append(cur.left)
                    stack.append('(')
        return ''.join([str(r) for r in res])


s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
print('1(2(4))(3)')
print('1(2(4))(3)' == s.tree2str(root))
print('1(2(4))(3)' == s.tree2strIter(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
print('1(2()(4))(3)')
print('1(2()(4))(3)' == s.tree2str(root))
print('1(2()(4))(3)' == s.tree2strIter(root))
