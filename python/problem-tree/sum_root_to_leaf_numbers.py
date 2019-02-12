#   https://leetcode.com/problems/sum-root-to-leaf-numbers


from TreeNode import TreeNode

class Solution:
    #   runtime; 36ms, 100.00%
    #   memory; 12.5MB, 0.93%
    def sumNumbers(self, root):
        if root is None:
            return 0
        ret, q = 0, [(0, root)]
        while q:
            parentsValue, node = q.pop(0)
            curVal = parentsValue + node.val
            if node.left or node.right:
                if node.left:
                    q.append((curVal * 10, node.left))
                if node.right:
                    q.append((curVal * 10, node.right))
            else:
                ret += curVal
        return ret


s = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root2 = TreeNode(4)
root2.left = TreeNode(9)
root2.right = TreeNode(0)
root2.left.left = TreeNode(5)
root2.left.right = TreeNode(1)
data = [(root1, 25),
        (root2, 1026),
        ]
for root, expected in data:
    real = s.sumNumbers(root)
    print('{}, expected {}, real {}, result {}'.format(root, expected, real, expected == real))
