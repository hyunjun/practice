#   https://leetcode.com/problems/maximum-width-of-binary-tree

#   https://leetcode.com/problems/maximum-width-of-binary-tree/solution


from TreeNode import TreeNode

class Solution:
    #   Wrong Answer
    def widthOfBinaryTree0(self, root):
        if root is None:
            return 0
        print(root)
        width, nodes, curDepth, q = 0, [], 0, [(0, root)]
        while q:
            depth, node = q.pop(0)
            if depth != curDepth:
                curDepth = depth
                while nodes[0] is None:
                    nodes.pop(0)
                while nodes[-1] is None:
                    nodes.pop()
                width = max(width, len(nodes))
                nodes = [node]
            else:
                nodes.append(node)
            if node:
                if node.left or node.right:
                    q.append((depth + 1, node.left))
                    q.append((depth + 1, node.right))
            print(nodes)
        while nodes[0] is None:
            nodes.pop(0)
        while nodes[-1] is None:
            nodes.pop()
        width = max(width, len(nodes))
        return width

    #   Wrong Answer
    def widthOfBinaryTree1(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        def getWidth(width, minW, maxW):
            if minW == maxW:
                return max(width, 1)
            return max(width, maxW - minW + 1)

        width, curDepth, minW, maxW, q = 0, 0, 0, 0, [(0, 1, root)]
        while q:
            depth, pos, node = q.pop(0)
            print(depth, pos, node.val)
            if curDepth != depth:
                width = getWidth(width, minW, maxW)
                curDepth, minW, maxW = depth, pos, pos
            else:
                maxW = pos
            if node.left:
                q.append((depth + 1, pos * 2, node.left))
            if node.right:
                q.append((depth + 1, pos * 2 + 1, node.right))
        width = getWidth(width, minW, maxW)
        return width

    #   runtime; 40ms, 100.00%
    #   memory; 13MB, 100.00%
    def widthOfBinaryTree(self, root):
        if root is None:
            return 0

        nodesDict, prevDepth, q = {}, -1, [(0, 1, root)]
        while q:
            depth, pos, node = q.pop(0)
            if prevDepth != depth:
                prevDepth = depth
                nodesDict[depth] = [pos, pos]
            else:
                nodesDict[depth][1] = pos
            if node.left:
                q.append((depth + 1, pos * 2, node.left))
            if node.right:
                q.append((depth + 1, pos * 2 + 1, node.right))
        print(nodesDict)
        return max([maxPos - minPos + 1 for minPos, maxPos in nodesDict.values()])

s = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)
root1.left.right = TreeNode(3)
root1.right.right = TreeNode(9)
root2 = TreeNode(1)
root2.left = TreeNode(3)
root2.left.left = TreeNode(5)
root2.left.right = TreeNode(3)
root3 = TreeNode(1)
root3.left = TreeNode(3)
root3.right = TreeNode(2)
root3.left.left = TreeNode(5)
root4 = TreeNode(1)
root4.left = TreeNode(1)
root4.right = TreeNode(1)
root4.left.left = TreeNode(1)
root4.right.right = TreeNode(1)
root4.left.left.left = TreeNode(1)
root4.right.right.right = TreeNode(1)
root5 = TreeNode(1)
root6 = TreeNode(1)
root6.left = TreeNode(2)
root7 = TreeNode(1)
root7.left = TreeNode(3)
root7.right = TreeNode(2)
root7.left.left = TreeNode(5)
data = [(root1, 4),
        (root2, 2),
        (root3, 2),
        (root4, 8),
        (root5, 1),
        (root6, 1),
        (root7, 2),
        ]
for root, expected in data:
    real = s.widthOfBinaryTree(root)
    print('{}, expected {}, real {}, result {}'.format(root, expected, real, expected == real))
