#   https://leetcode.com/problems/univalued-binary-tree

#   https://leetcode.com/problems/univalued-binary-tree/solution


from TreeNode import TreeNode


class Solution:
    #   56ms, 86.17%
    def isUnivalTree(self, root):
        q, n, s = [], root, set()
        while q or n:
            if n:
                q.append(n)
                n = n.left
            else:
                n = q.pop()
                s.add(n.val)
                if 1 < len(s):
                    return False
                n = n.right
        return True
