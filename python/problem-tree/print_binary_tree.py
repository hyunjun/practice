#   https://leetcode.com/problems/print-binary-tree

#   https://leetcode.com/problems/print-binary-tree/solution


from TreeNode import TreeNode

class Solution:
    #   runtime; 40ms, 99.36%
    #   memory; 12.4MB, 100.00%
    def printTree(self, root):
        if root is None:
            return [[]]
        maxDepth, q = 0, [(1, root)]
        while q:
            depth, node = q.pop(0)
            maxDepth = max(maxDepth, depth)
            if node.left:
                q.append((depth + 1, node.left))
            if node.right:
                q.append((depth + 1, node.right))
        width = sum([2 ** d for d in range(maxDepth)])
        res = [[""] * width for _ in range(maxDepth)]
        q = [(width // 2, 0, root)]
        while q:
            x, y, node = q.pop(0)
            xDiff = int(2 ** (maxDepth - 2 - y))
            print(x, y, node.val, xDiff)
            res[y][x] = str(node.val)
            if node.left:
                q.append((x - xDiff, y + 1, node.left))
            if node.right:
                q.append((x + xDiff, y + 1, node.right))
        print(res)
        return res


s = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(5)
root3.left.left = TreeNode(3)
root3.left.left.left = TreeNode(4)
data = [(root1, [["", "1", ""], ["2", "", ""]]),
        (root2, [["", "", "", "1", "", "", ""], ["", "2", "", "", "", "3", ""], ["", "", "4", "", "", "", ""]]),
        (root3, [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""], ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""], ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""], ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]),
        ]
for root, expected in data:
    real = s.printTree(root)
    print('{}, expected row {} column {}, real row {} column {}, result {}'.format(root, len(expected), len(expected[0]), len(real), len(real[0]), len(expected) == len(real) and len(expected[0]) == len(real[0])))
