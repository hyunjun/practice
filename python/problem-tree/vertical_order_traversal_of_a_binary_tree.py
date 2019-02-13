#   https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree

#   https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/solution


from TreeNode import TreeNode
from collections import defaultdict

class Solution:
    #   runtime; 36ms, 100.00%
    #   memory; 12.8MB, 100.00%
    def verticalTraversal(self, root):
        if root is None:
            return []
        levelOrderTraverse, q = defaultdict(list), [(0, 0, root)]
        while q:
            x, y, node = q.pop(0)
            print(x, y, node.val)
            levelOrderTraverse[x].append((y, node.val))
            if node.left:
                q.append((x - 1, y - 1, node.left))
            if node.right:
                q.append((x + 1, y - 1, node.right))
        print(levelOrderTraverse)
        return [[v for _, v in sorted(val, key=lambda t: (-t[0], t[1]))] for _, val in sorted(levelOrderTraverse.items(), key=lambda t: t[0])]


s = Solution()
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(7)
root3 = TreeNode(0)
root3.left = TreeNode(2)
root3.right = TreeNode(1)
root3.left.left = TreeNode(3)
root3.left.left.left = TreeNode(4)
root3.left.left.right = TreeNode(5)
root3.left.left.left.right = TreeNode(7)
root3.left.left.right.left = TreeNode(6)
root3.left.left.left.right.left = TreeNode(10)
root3.left.left.left.right.right = TreeNode(8)
root3.left.left.right.left.left = TreeNode(11)
root3.left.left.right.left.right = TreeNode(9)
root4 = TreeNode(0)
root4.left = TreeNode(5)
root4.right = TreeNode(1)
root4.left.left = TreeNode(9)
root4.right.left = TreeNode(2)
root4.right.left.right = TreeNode(3)
root4.right.left.right.left = TreeNode(4)
root4.right.left.right.right = TreeNode(8)
root4.right.left.right.left.left = TreeNode(6)
root4.right.left.right.left.left.left = TreeNode(7)
data = [(root1, [[9], [3, 15], [20], [7]]),
        (root2, [[4], [2], [1, 5, 6], [3], [7]]),
        (root3, [[4,10,11],[3,6,7],[2,5,8,9],[0],[1]]),
        (root4, [[9,7],[5,6],[0,2,4],[1,3],[8]]),
        ]
for root, expected in data:
    real = s.verticalTraversal(root)
    print('{}, expected {}, real {}, result {}'.format(root, expected, real, expected == real))
