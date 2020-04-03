#   https://leetcode.com/problems/balance-a-binary-search-tree


from TreeNode import TreeNode


class Solution:
    #   runtime; 388ms, 22.10%
    #   memory; 20MB, 100.00%
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return []

        n, s, r = root, [], []
        while s or n:
            if n:
                s.append(n)
                n = n.left
            else:
                n = s.pop()
                r.append(n.val)
                n = n.right

        def makeBST(l):
            print(l)
            if 0 == len(l):
                return None
            m = len(l) // 2
            n = TreeNode(l[m])
            n.left, n.right = makeBST(l[:m]), makeBST(l[m + 1:])
            return n

        return makeBST(r)


s = Solution()
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.right = TreeNode(3)
root1.right.right.right = TreeNode(4)
print(s.balanceBST(root1))
