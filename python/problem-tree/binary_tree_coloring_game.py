#   https://leetcode.com/problems/binary-tree-coloring-game


from TreeNode import TreeNode


class Solution:
    #   runtime; 40ms, 66.67%
    #   memory; 13.9MB, 100.00%
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        if root is None:
            return False

        def getCount(node):
            if node is None:
                return 0
            return 1 + getCount(node.left) + getCount(node.right)

        q = [root]
        while q:
            node = q.pop()
            if node.val == x:
                lCount, rCount = getCount(node.left), getCount(node.right)
                if lCount > n / 2 or rCount > n / 2 or n - (1 + lCount + rCount) > n / 2:
                    return True
                break
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False


s = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)
root1.left.left.left = TreeNode(8)
root1.left.left.right = TreeNode(9)
root1.left.right.left = TreeNode(10)
root1.left.right.right = TreeNode(11)
data = [(root1, 11, 3, True),
        ]
for root, n, x, expected in data:
    real = s.btreeGameWinningMove(root, n, x)
    print(f'{root}, {n}, {x}, expected {expected}, real {real}, result {expected == real}')
