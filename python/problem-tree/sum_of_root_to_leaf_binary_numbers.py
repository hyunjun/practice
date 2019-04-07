#   https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers


from TreeNode import TreeNode


class Solution:
    #   runtime; 48ms, 100.00%
    #   memory; 13.4MB, 100.00%
    def sumRootToLeaf(self, root):
        if root is None:
            return 0
        q, _sum = [([], root)], 0
        while q:
            parents, node = q.pop(0)
            if node.left or node.right:
                parents.append(node.val)
                if node.left:
                    q.append((parents[:], node.left))
                if node.right:
                    q.append((parents[:], node.right))
            else:
                parents.append(node.val)
                depth = len(parents)
                for i, b in enumerate(parents):
                    if 0 == b:
                        continue
                    _sum += 2 ** (depth - i - 1)
        return _sum


s = Solution()
root = TreeNode(1)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)
print(s.sumRootToLeaf(root) == 22)
