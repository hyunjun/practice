#   https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree


from TreeNode import TreeNode
from collections import defaultdict


class Solution:
    #   runtime; 436ms, 66.67%
    #   memory; 49.5MB, 100.00%
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        if root is None:
            return 0

        def isPalindrome(arr, counter):
            oddVal, oddCnt = None, 0
            for n, cnt in counter.items():
                if cnt % 2 == 1:
                    oddCnt += 1
                    oddVal = n
                    if oddCnt > 1:
                        return False
            return True

        self.cnt = 0

        def getPaths(acc, counter, node):
            if node is None:
                return
            acc.append(node.val)
            counter[node.val] += 1
            if node.left or node.right:
                getPaths(acc, counter, node.left)
                getPaths(acc, counter, node.right)
            else:
                if isPalindrome(acc, counter):
                    self.cnt += 1
            acc.pop()
            counter[node.val] -= 1

        getPaths([], defaultdict(int), root)

        return self.cnt


s = Solution()
root1 = TreeNode(2)
root1.left = TreeNode(3)
root1.right = TreeNode(1)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(1)
root1.right.right = TreeNode(1)
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(1)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(3)
root2.left.right.right = TreeNode(1)
data = [(root1, 2),
        (root2, 1),
        ]
for root, expect in data:
    real = s.pseudoPalindromicPaths(root)
    print(f'{root} expect {expect} real {real} result {expect == real}')
