#   https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers


from TreeNode import TreeNode


class Solution:
    #   runtime; 48ms, 100.00%
    #   memory; 13.4MB, 100.00%
    def sumRootToLeaf0(self, root):
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

    #   runtime; 48ms, 100.00%
    #   memory; 13.4MB, 100.00%
    def sumRootToLeaf1(self, root):
        if root is None:
            return 0
        root.parent = None
        q, leaves = [root], []
        while q:
            n = q.pop(0)
            if n.left or n.right:
                if n.left:
                    n.left.parent = n
                    q.append(n.left)
                if n.right:
                    n.right.parent = n
                    q.append(n.right)
            else:
                leaves.append(n)
        _sum = 0
        for leaf in leaves:
            n, times = leaf, 1
            while n:
                if 1 == n.val:
                    _sum += times
                times *= 2
                n = n.parent
        return _sum

    #   https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3453
    #   runtime; 48ms, 33.94%
    #   memory; 14.1MB, 33.41%
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.res = 0
        def getLeafSum(acc, node):
            acc.append(node.val)
            if node.left is None and node.right is None:
                self.res += sum(v *  2 ** (len(acc) - i - 1) for i, v in enumerate(acc))
            else:
                if node.left:
                    getLeafSum(acc[:], node.left)
                if node.right:
                    getLeafSum(acc[:], node.right)
        if root:
            getLeafSum([], root)
        return self.res


s = Solution()
root = TreeNode(1)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)
data = [(root, 22),
        ]
for root, expect in data:
    real = s.sumRootToLeaf(root)
    print(f'{root} expect {expect} real {real} result {expect == real}')
