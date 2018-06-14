#   https://leetcode.com/problems/minimum-depth-of-binary-tree


from TreeNode import TreeNode
import sys


class Solution:
    def minDepth(self, root):
        #return self.minDepthRecur(root)
        return self.minDepthIter(root)

    #   99.23%
    def minDepthRecur(self, node):
        if node is None:
            return 0
        lDepth, rDepth = self.minDepthRecur(node.left), self.minDepthRecur(node.right)
        if 0 == lDepth:
            return rDepth + 1
        if 0 == rDepth:
            return lDepth + 1
        return min(lDepth, rDepth) + 1

    #   93.86%
    def minDepthIter(self, node):
        if node is None:
            return 0
        queue, minLevel = [(node, 1)], sys.maxsize
        while queue:
            cur, curLevel = queue[0]
            del queue[0]
            if cur.left is None and cur.right is None:
                if curLevel < minLevel:
                    minLevel = curLevel
            if cur.left:
                queue.append((cur.left, curLevel + 1))
            if cur.right:
                queue.append((cur.right, curLevel + 1))
        return minLevel


s = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(s.minDepth(root))

root = TreeNode(1)
root.right = TreeNode(2)
print(s.minDepth(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
print(s.minDepth(root))
