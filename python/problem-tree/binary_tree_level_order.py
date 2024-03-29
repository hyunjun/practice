# https://leetcode.com/problems/binary-tree-level-order-traversal/


from TreeNode import TreeNode


class Solution(object):
  def levelOrder(self, root):
    if root is None:
      return []
    q, result = [(root, 1)], []
    while 0 < len(q):
      cur, level = q[0]
      if len(result) < level:
        result.append([cur.val])
      else:
        result[level - 1].append(cur.val)
      if cur.left is not None:
        q.append((cur.left, level + 1))
      if cur.right is not None:
        q.append((cur.right, level + 1))
      del q[0]
    return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(9)
root.right.right.right.left = TreeNode(11)

s = Solution()
print(s.levelOrder(root))
