#   https://leetcode.com/problems/maximum-depth-of-binary-tree


from TreeNode import TreeNode


class Solution:
    def maxDepth0(self, root):
        #return self.maxDepthRecur(root)
        return self.maxDepthIter(root)

    #   77.46%
    def maxDepthRecur(self, node):
        if node is None:
            return 0
        return max(self.maxDepthRecur(node.left) + 1, self.maxDepthRecur(node.right) + 1)

    #   95.76%
    def maxDepthIter(self, node):
        if node is None:
            return 0
        queue, maxLevel = [(node, 1)], 0
        while queue:
            cur, curLevel = queue[0]
            del queue[0]
            if maxLevel < curLevel:
                maxLevel = curLevel
            if cur.left:
                queue.append((cur.left, curLevel + 1))
            if cur.right:
                queue.append((cur.right, curLevel + 1))
        return maxLevel

    #   https://leetcode.com/explore/featured/card/recursion-i/256/complexity-analysis/2375
    #   runtime; 36ms, 89.85%
    #   memory; 15.8MB
    def maxDepth(self, root):
        def getDepth(n):
            if n is None:
                return 0
            return 1 + max(getDepth(n.left), getDepth(n.right))

        return getDepth(node)


s = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(s.maxDepth(root))
