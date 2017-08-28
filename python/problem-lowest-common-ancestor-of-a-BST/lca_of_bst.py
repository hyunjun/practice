# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
# 10.40%
import sys

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if root is None:
      return None

    if p.val > q.val:
      p, q = q, p
    cur, stack = (root, 0), []
    pResult, qResult, result = False, False, []
    while 0 < len(stack) or cur is not None:
      if cur is not None:
        stack.append(cur)
        if cur[0].left is None:
          cur = None
        else:
          cur = (cur[0].left, cur[1] + 1)
      else:
        cur, depth = stack.pop()
        if cur.val == p.val:
          pResult = True
        elif cur.val == q.val:
          qResult = True
        if pResult:
          result.append((cur, depth))
          if qResult:
            break
        if cur.right is None:
          cur = None
        else:
          cur = (cur.right, depth + 1)

    minHeight, lcaNode = sys.maxsize, None
    for n, depth in result:
      if depth < minHeight:
        minHeight = depth
        lcaNode = n
    return lcaNode



'''
        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
'''
root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.left = TreeNode(5)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.left = TreeNode(9)

s = Solution()
result = s.lowestCommonAncestor(root, root.left, root.right)
print(result.val)
result = s.lowestCommonAncestor(root, root.left, root.left.right.left)
print(result.val)

root = TreeNode(2)
root.right = TreeNode(3)
result = s.lowestCommonAncestor(root, root.right, root)
print(result.val)
