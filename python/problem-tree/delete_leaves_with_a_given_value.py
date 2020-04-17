#   https://leetcode.com/problems/delete-leaves-with-a-given-value


from TreeNode import TreeNode


class Solution:
    #   runtime; 48ms, 90.35%
    #   memory; 14.2MB, 100.00%
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root is None:
            return None

        def removeNode(node):
            if node.left:
                node.left = removeNode(node.left)
            if node.right:
                node.right = removeNode(node.right)
            if node.left is None and node.right is None and node.val == target:
                node = None
            return node

        return removeNode(root)


s = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.left.left = TreeNode(2)
root1.right = TreeNode(3)
root1.right.left = TreeNode(2)
root1.right.right = TreeNode(4)
deletedRoot1 = TreeNode(1)
deletedRoot1.right = TreeNode(3)
deletedRoot1.right.right = TreeNode(4)
root2 = TreeNode(1)
root2.left = TreeNode(3)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(2)
root2.right = TreeNode(3)
deletedRoot2 = TreeNode(1)
deletedRoot2.left = TreeNode(3)
deletedRoot2.left.right = TreeNode(2)
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.left.left = TreeNode(2)
root3.left.left.left = TreeNode(2)
deletedRoot3 = TreeNode(1)
root4 = TreeNode(1)
root4.left = TreeNode(1)
root4.right = TreeNode(1)
root5 = TreeNode(1)
root5.left = TreeNode(2)
root5.right = TreeNode(3)
data = [(root1, 2, deletedRoot1),
        (root2, 3, deletedRoot2),
        (root3, 2, deletedRoot3),
        (root4, 1, None),
        (root5, 1, root5),
        ]
for root, target, expected in data:
    real = s.removeLeafNodes(root, target)
    print(f'{root} {target} exepcted {expected} real {real} result {expected == real}')
'''
if node is leaf & node.val == target:
    node = None
    back to parent node
'''
