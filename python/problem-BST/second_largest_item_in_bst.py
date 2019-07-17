#   https://www.interviewcake.com/question/python/second-largest-item-in-bst


from TreeNode import TreeNode


class Solution:
    def secondLargestItem(self, root):
        if root is None or (root.left is None and root.right is None):
            return None

        def getLargestItem(node):
            parent = None
            while node.right:
                parent, node = node, node.right
            return parent, node

        parent, largest = getLargestItem(root)
        if largest.left:
            _, secondLargest = getLargestItem(largest.left)
            return secondLargest.val
        return parent.val


s = Solution()

root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(4)
root1.right = TreeNode(7)
root1.right.right = TreeNode(9)
root1.right.right.left = TreeNode(8)

root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(4)
root2.right = TreeNode(7)
root2.right.right = TreeNode(8)
root2.right.right.right = TreeNode(9)

root3 = TreeNode(5)
root3.left = TreeNode(3)
root3.left.left = TreeNode(1)
root3.left.right = TreeNode(4)
root3.right = TreeNode(9)
root3.right.left = TreeNode(8)
root3.right.left.left = TreeNode(7)

root4 = TreeNode(5)
root4.left = TreeNode(3)
root4.left.left = TreeNode(1)
root4.left.right = TreeNode(4)
root4.right = TreeNode(8)
root4.right.left = TreeNode(7)
root4.right.right = TreeNode(12)
root4.right.right.left = TreeNode(10)
root4.right.right.left.left = TreeNode(9)
root4.right.right.left.right = TreeNode(11)

for root, expected in [(root1, 8), (root2, 8), (root3, 8), (root4, 11)]:
    real = s.secondLargestItem(root)
    print(f'{root}, expected {expected}, real {real}, result {expected == real}')
