#   https://leetcode.com/problems/validate-binary-search-tree


from TreeNode import TreeNode


class Solution(object):
    #   runtime; 69ms, 51.98%
    def isValidBST0(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        cur, stack, values = root, [], []
        while cur is not None or 0 < len(stack):
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                values.append(cur.val)
                cur = cur.right
        for i in range(1, len(values)):
            if values[i - 1] >= values[i]:
                return False
        return True

    _MIN, _MAX = -99999999, 99999999
    def isValidBST1(self, root):
        def isValidBSTRecur(node, _min, _max):
            if node is None:
                return True
            lResult = True
            if node.left is not None:
                if node.left.val < node.val < _max:
                    lResult = isValidBSTRecur(node.left, Solution._MIN, node.val)
                else:
                    return False
            rResult = True
            if node.right is not None:
                if _min < node.val < node.right.val:
                    rResult = isValidBSTRecur(node.right, node.val, Solution._MAX)
                else:
                    return False
            return lResult and rResult

        return isValidBSTRecur(root, Solution._MIN, Solution._MAX)

    #   runtime; 28ms, 94.05%
    #   memory; 16.5MB, 50.94%
    def isValidBST2(self, root):

        def _isBST(node, _min, _max):
            if node is None:
                return True
            if not (_min < node.val < _max):
                return False
            if node.left and node.left.val >= node.val:
                return False
            if node.right and node.val >= node.right.val:
                return False
            return _isBST(node.left, _min, node.val) and _isBST(node.right, node.val, _max)

        return _isBST(root, -float('inf'), float('inf'))

    #   runtime; 40ms, 31.90%
    #   memory; 16.1MB, 100.00%
    def isValidBST(self, root):
        if root is None:
            return True

        q = [(root, -float('inf'), float('inf'))]
        while q:
            node, _min, _max = q.pop(0)
            if not (_min < node.val < _max):
                return False
            if node.left:
                if node.left.val >= node.val:
                    return False
                q.append((node.left, _min, node.val))
            if node.right:
                if node.val >= node.right.val:
                    return False
                q.append((node.right, node.val, _max))
        return True


s = Solution()

root0 = TreeNode(2)
root0.left = TreeNode(1)
root0.right = TreeNode(3)

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(4)
root2.right = TreeNode(7)
root2.right.right = TreeNode(9)
root2.right.right.left = TreeNode(8)

root3 = TreeNode(10)
root3.left = TreeNode(5)
root3.right = TreeNode(15)
root3.right.left = TreeNode(6)
root3.right.right = TreeNode(20)

data = [(root0, True),
        (root1, False),
        (root2, True),
        (root3, False),
        ]
for root, expected in data:
  real = s.isValidBST(root)
  print(f'{root}, expected {expected}, real {real}, result {expected == real}')
