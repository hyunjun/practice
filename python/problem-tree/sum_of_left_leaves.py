#   https://leetcode.com/problems/sum-of-left-leaves

#   https://leetcode.com/problems/sum-of-left-leaves/discuss/133053/Python-5-line-Simple-recursive-solution


from TreeNode import TreeNode


class Solution:
    #   25.21%
    def sumOfLeftLeaves0(self, root):
        if root is None:
            return 0
        queue, res = [(root, False)], 0
        while queue:
            cur, isLeft = queue[0]
            del queue[0]
            if isLeft and cur.left is None and cur.right is None:
                res += cur.val
            if cur.left:
                queue.append((cur.left, True))
            if cur.right:
                queue.append((cur.right, False))
        return res

    #   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3435
    #   runtime; 36ms, 60.61%
    #   memory; 13.9MB, 97.49%
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        res, q = 0, [(root, False)]
        while q:
            n, isLeft = q.pop(0)
            if isLeft and not n.left and not n.right:
                res += n.val
            if n.left:
                q.append((n.left, True))
            if n.right:
                q.append((n.right, False))
        return res


s = Solution()

'''
    3
   / \
  9  20
    /  \
   15   7
'''
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
data = [(root, 24),
        ]
for root, expect in data:
    real = s.sumOfLeftLeaves(root)
    print(f'{root} expect {expect} real {real} result {expect == real}')
