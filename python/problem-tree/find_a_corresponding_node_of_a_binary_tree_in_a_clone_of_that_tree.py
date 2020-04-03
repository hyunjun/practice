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
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
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
