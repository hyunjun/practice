#   https://leetcode.com/problems/flatten-binary-tree-to-linked-list
#   50.26%

class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def flatten(self, node):
    if node is None:
      return None
    if node.left is None:
      return self.flatten(node.right)
    if node.right is not None:
      rightmostOfLeft = node.left
      while rightmostOfLeft.right is not None:
        rightmostOfLeft = rightmostOfLeft.right
      rightmostOfLeft.right = node.right
      node.right = None
    node.right = node.left
    node.left = None
    return self.flatten(node.right)


def printTree(node):
  if node is None:
    return ''
  return '({}({}){})'.format(printTree(node.left), node.val, printTree(node.right))


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)

print(printTree(root))
s = Solution()
s.flatten(root)
print(printTree(root))
