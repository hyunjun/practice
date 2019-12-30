#   https://leetcode.com/problems/all-elements-in-two-binary-search-trees/


from TreeNode import TreeNode
from typing import List


class Solution:
    #   runtime; 332ms, 93.03%
    #   memory; 16MB, 100.00%
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def elems(node):
            n, stack, res = node, [], []
            while n or stack:
                if n:
                    stack.append(n)
                    n = n.left
                else:
                    n = stack.pop()
                    res.append(n.val)
                    n = n.right
            return res

        res = elems(root1)
        res.extend(elems(root2))
        return sorted(res)


s = Solution()
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(3)
data = [(root1, root2, [0, 1, 1, 2, 3, 4]),
        (None, None, []),
        ]
for root1, root2, expected in data:
    real = s.getAllElements(root1, root2)
    print(f'{root1} {root2} expected {expected} real {real} result {expected == real}')
