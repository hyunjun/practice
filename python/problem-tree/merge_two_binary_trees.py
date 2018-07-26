#   https://leetcode.com/problems/merge-two-binary-trees

#   https://leetcode.com/problems/merge-two-binary-trees/solution


from TreeNode import TreeNode


class Solution:
    #   9.40%   124ms
    def mergeTrees(self, t1, t2):
        def merge(n1, n2):
            if n1 is None and n2 is None:
                return None
            node = TreeNode(0)
            node.val = n1.val if n1 else 0
            node.val += n2.val if n2 else 0
            node.left = merge(n1.left if n1 else None, n2.left if n2 else None)
            node.right = merge(n1.right if n1 else None, n2.right if n2 else None)
            return node
        return merge(t1, t2)

    #   0.00%?  192ms
    def mergeTreesIter(self, t1, t2):
        if t1 is None and t2 is None:
            return None
        root = TreeNode(0)
        q = [(root, t1, t2)]
        while q:
            cur, n1, n2 = q.pop(0)
            cur.val = n1.val if n1 else 0
            cur.val += n2.val if n2 else 0
            n1L, n2L = n1.left if n1 else None, n2.left if n2 else None
            if n1L or n2L:
                cur.left = TreeNode(0)
                q.append((cur.left, n1L, n2L))
            n1R, n2R = n1.right if n1 else None, n2.right if n2 else None
            if n1R or n2R:
                cur.right = TreeNode(0)
                q.append((cur.right, n1R, n2R))
        return root


s = Solution()

t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.right = TreeNode(2)
t1.left.left = TreeNode(5)
t2 = TreeNode(2)
t2.left = TreeNode(1)
t2.right = TreeNode(3)
t2.left.right = TreeNode(4)
t2.right.right = TreeNode(7)
print(s.mergeTrees(t1, t2))
print(s.mergeTreesIter(t1, t2))
