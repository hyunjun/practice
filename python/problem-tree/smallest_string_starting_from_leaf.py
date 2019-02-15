#   https://leetcode.com/problems/smallest-string-starting-from-leaf

#   https://leetcode.com/problems/smallest-string-starting-from-leaf/solution


from TreeNode import TreeNode

class Solution:
    #   runtime; 32ms, 41.88%
    #   memory; 11.5MB, 100.00%
    def smallestFromLeaf(self, root):
        if root is None:
            return ''
        leaves, q = [], [([], root)]
        while q:
            parents, node = q.pop(0)
            if node.left is None and node.right is None:
                leaf = [chr(97 + node.val)]
                leaf.extend([chr(97 + p) for p in parents[::-1]])
                leaves.append(''.join(leaf))
            parents.append(node.val)
            if node.left:
                q.append((parents[:], node.left))
            if node.right:
                q.append((parents[:], node.right))
            parents.pop()
        return sorted(leaves)[0]


s = Solution()
root1 = TreeNode(0)
root1.left = TreeNode(1)
root1.right = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(3)
root1.right.right = TreeNode(4)
root2 = TreeNode(25)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(3)
root2.right.left = TreeNode(0)
root2.right.right = TreeNode(2)
root3 = TreeNode(2)
root3.left = TreeNode(2)
root3.right = TreeNode(1)
root3.left.right = TreeNode(1)
root3.right.left = TreeNode(0)
root3.left.right.left = TreeNode(0)
data = [(root1, 'dba'),
        (root2, 'adz'),
        (root3, 'abc'),
        ]
for root, expected in data:
    real = s.smallestFromLeaf(root)
    print('{}, expected {}, real {}, result {}'.format(root, expected, real, expected == real))
