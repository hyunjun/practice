#   https://leetcode.com/problems/validate-binary-search-tree
#   51.98%


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
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
    def isValidBST2(self, root):
        def isValidBSTRecur(node, _min, _max):
            if node is None:
                return True
            lResult = True
            if node.left is not None:
                print(node.left.val, node.val, _max)
                if node.left.val < node.val < _max:
                    lResult = isValidBSTRecur(node.left, Solution._MIN, node.val)
                else:
                    return False
            rResult = True
            if node.right is not None:
                print(_min, node.val, node.right.val)
                if _min < node.val < node.right.val:
                    rResult = isValidBSTRecur(node.right, node.val, Solution._MAX)
                else:
                    return False
            print('l result {}\tr result {}\tl result and r result {}'.format(lResult, rResult, lResult and rResult))
            return lResult and rResult

        return isValidBSTRecur(root, Solution._MIN, Solution._MAX)


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

roots = [root0, root1, root2, root3]
for root in roots:
  print(s.isValidBST(root), s.isValidBST2(root))
