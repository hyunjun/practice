# https://leetcode.com/problems/binary-tree-paths/
# 66.62%

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def binaryTreePaths(self, root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    if root is None:
      return []

    cur, stack, result = (root, []), [], []
    while 0 < len(stack) or (cur is not () and cur[0] is not None):
      if cur is not () and cur[0] is not None:
        stack.append(cur)
        curNode, prevs = cur[0].left, cur[1][:]
        prevs.append(cur[0].val)
        cur = (curNode, prevs)
      else:
        print('stack {}'.format(stack))
        curNode, prevs = stack.pop()
        nextPrevs = prevs[:]
        nextPrevs.append(curNode.val)
        if curNode.left is None and curNode.right is None:
          result.append(nextPrevs)
          print(result)
        cur = (curNode.right, nextPrevs)
        print('cur {}'.format(cur))
    return ['->'.join([str(n) for n in r]) for r in result]


root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)

s = Solution()
print(s.binaryTreePaths(root))
