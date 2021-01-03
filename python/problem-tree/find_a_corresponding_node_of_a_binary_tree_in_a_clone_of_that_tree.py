#   https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree


from TreeNode import TreeNode


class Solution:
    #   runtime; 700ms, 17.84%
    #   memory; 23.3MB, 100.00%
    def getTargetCopy0(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        oq, cq = [original], [cloned]
        while oq:
            on, cn = oq.pop(0), cq.pop(0)
            if on == target:
                return cn
            if on.left:
                oq.append(on.left)
                cq.append(cn.left)
            if on.right:
                oq.append(on.right)
                cq.append(cn.right)
        return None

    #   runtime; 636ms, 97.89%
    #   memory; 23.5MB, 100.00%
    def getTargetCopy1(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = [(original, cloned)]
        while q:
            on, cn = q.pop(0)
            if on == target:
                return cn
            if on.left:
                q.append((on.left, cn.left))
            if on.right:
                q.append((on.right, cn.right))
        return None

    #   https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3590
    #   runtime; 672ms, 12.63%
    #   memory; 24.2MB, 11.50%
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q1, q2 = [original], [cloned]
        while q1 and q2:
            n1, n2 = q1.pop(), q2.pop()
            if n1 == target:
                return n2
            if n1.left and n2.left:
                q1.append(n1.left)
                q2.append(n2.left)
            if n1.right and n2.right:
                q1.append(n1.right)
                q2.append(n2.right)
        return None
