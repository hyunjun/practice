#   https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes

#   https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/solution


from TreeNode import TreeNode

class Solution:
    #   runtime; 36ms, 100.00%
    #   memory; 12.7MB, 0.97%
    def subtreeWithAllDeepest(self, root):
        if root is None:
            return None
        '''
        traverse the tree
            to get the deepest depth of the tree
            to save the current depth, and its nodes (list)
            to save the parents of all the nodes, key is a val of node, value is a TreeNode (dictionary)
        get the parents list of nodes which have the deepest depth from dictionary
        '''
        maxDepth, maxDepthNodes, parentDict, q = -1, [], {}, [(0, None, root)]
        while q:
            depth, parent, node = q.pop(0)
            parentDict[node] = parent
            if maxDepth < depth:
                maxDepth, maxDepthNodes = depth, [node]
            elif maxDepth == depth:
                maxDepthNodes.append(node)
            if node.left:
                q.append((depth + 1, node, node.left))
            if node.right:
                q.append((depth + 1, node, node.right))
        if 1 == len(maxDepthNodes):
            return maxDepthNodes[0]
        parentsListOfList = []
        for i, maxDepthNode in enumerate(maxDepthNodes):
            node, l = maxDepthNode, []
            while node in parentDict:
                l.append(parentDict[node])
                node = parentDict[node]
            parentsListOfList.append(l)
        for i in range(len(parentsListOfList[0])):
            s = set([parentsListOfList[j][i] for j in range(len(parentsListOfList))])
            if 1 == len(s):
                return parentsListOfList[0][i]
        return None


s = Solution()
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.right.left = TreeNode(0)
root1.right.right = TreeNode(8)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)
print(s.subtreeWithAllDeepest(root1))
'''
q = (depth parent node) parentDict maxDepth maxDepthNodes
    0       x       3   3:x         -1 > 0  [3]
    1       3       5   5:3         0 > 1   [5]
    1       3       1   1:3         1 == 1  [5, 1]
    2       5       6   6:5         1 > 2   [6]
    2       5       2   2:5         2 == 2  [6, 2]
    2       1       0   0:1         2 == 2  [6, 2, 0]
    2       1       8   8:1         2 == 2  [6, 2, 0, 8]
    3       2       7   7:2         2 > 3   [7]
    3       2       4   4:2         3 == 3  [7, 4]
node
7       [0] = [2]
2       [0] = [2, 5]
5       [0] = [2, 5, 3]
3       [0] = [2, 5, 3, None]
4       [1] = [2, 5, 3, None]
for i in range(4):
    s = set([[0][0], [1][0]])
    2
'''
print(s.subtreeWithAllDeepest(TreeNode(1)))

root2 = TreeNode(0)
root2.left = TreeNode(3)
root2.right = TreeNode(1)
root2.left.left = TreeNode(4)
root2.right.left = TreeNode(2)
root2.left.left.right = TreeNode(6)
root2.right.left.right = TreeNode(5)
print(s.subtreeWithAllDeepest(root2))
