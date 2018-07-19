#   https://leetcode.com/problems/diameter-of-binary-tree


from TreeNode import TreeNode


class Solution:
    #   Wrong Answer
    def diameterOfBinaryTree0(self, root):
        def getDepth(node):
            if node is None:
                return 0
            maxDepth, queue = 0, [(node, 1)]
            while queue:
                cur, depth = queue.pop(0)
                maxDepth = max(maxDepth, depth)
                if cur.left:
                    queue.append((cur.left, depth + 1))
                if cur.right:
                    queue.append((cur.right, depth + 1))
            return maxDepth

        if root is None or (root.left is None and root.right is None):
            return 0
        return getDepth(root.left) + getDepth(root.right)

    #   22.61%
    #   a kind of lowest common ancestor
    def diameterOfBinaryTree1(self, root):
        if root is None or (root.left is None and root.right is None):
            return 0
        queue, parentDict, edges = [(root, 0, None)], {}, []
        while queue:
            cur, depth, parent = queue.pop(0)
            parentDict[cur] = (depth, parent)
            if cur.left:
                queue.append((cur.left, depth + 1, cur))
            if cur.right:
                queue.append((cur.right, depth + 1, cur))
            if cur.left is None and cur.right is None:
                edges.append(cur)

        maxDepth, edgeDict = 0, {}
        for edge in edges[::-1]:
            print(edge.val)
            isFirstCommonAncestor = True
            edgeDepth, parent = parentDict[edge]
            while parent:
                parentDepth, parentParent = parentDict[parent]
                if parent in edgeDict:
                    prevEdge, prevLen = edgeDict[parent]
                    if isFirstCommonAncestor:
                        maxDepth = max(maxDepth, edgeDepth - parentDepth + prevLen)
                        print('update maxdepth as {} cur edge {} cur parent {}'.format(maxDepth, edge.val, parent.val))
                        isFirstCommonAncestor = False
                    if prevLen < edgeDepth - parentDepth:
                        edgeDict[parent] = (edge, edgeDepth - parentDepth)
                else:
                    edgeDict[parent] = (edge, edgeDepth - parentDepth)
                    maxDepth = max(maxDepth, edgeDepth - parentDepth)
                parent = parentParent
        return maxDepth

    #   https://leetcode.com/problems/diameter-of-binary-tree/solution
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L + R + 1)
            print('{} -> L {}, R {}, ans {}'.format(node.val, L, R, self.ans))
            return max(L, R) + 1
        depth(root)
        return self.ans - 1


s = Solution()
'''
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
'''
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print()
print(s.diameterOfBinaryTree(root)) #   3

'''
          0
         /
        1
       /
      2
     / \     
    4   5    
         \
          6
Return 3, which is the length of the path [4,2,5,6]
'''
root = TreeNode(0)
root.left = TreeNode(1)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(5)
root.left.left.right.right = TreeNode(6)
print()
print(s.diameterOfBinaryTree(root)) #   3

root = TreeNode(4)
root.left = TreeNode(-7)
root.right = TreeNode(-3)
root.right.left = TreeNode(-9)
root.right.left.left = TreeNode(9)
root.right.left.left.left = TreeNode(6)
root.right.left.left.left.left = TreeNode(0)
root.right.left.left.left.left.right = TreeNode(-1)
root.right.left.left.left.right = TreeNode(6)
root.right.left.left.left.right.left = TreeNode(-4)
root.right.left.right = TreeNode(-7)
root.right.left.right.left = TreeNode(-6)
root.right.left.right.left.left = TreeNode(5)
root.right.left.right.right = TreeNode(-6)
root.right.left.right.right.left = TreeNode(9)
root.right.left.right.right.left.left = TreeNode(-2)
root.right.right = TreeNode(-3)
root.right.right.left = TreeNode(-4)
print()
print(s.diameterOfBinaryTree(root)) #   8

root = TreeNode(1)
root.left = TreeNode(2)
print()
print(s.diameterOfBinaryTree(root)) #   1
